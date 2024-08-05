from .models import Stack, TakenProduct


def open_stack(request):
    # using this session code, program will id user's cart
    #  if no session_key is generated yet, then create one first
    stack_id = None
    try:
        if not request.session.session_key:  # solves the None session key error
            request.session.save()
        stack_id = request.session.session_key or request.session.create()

        if request.user.is_authenticated:
            if Stack.objects.all():
                merge_user_stacks(request.user)
                current_stack = Stack.objects.filter(belongs_to=request.user)
                # TEMP ***************
                if not current_stack:
                    raise Stack.DoesNotExist
                current_stack = current_stack[0]
            else:
                raise Stack.DoesNotExist

        else:
            current_stack = Stack.objects.get(sid=stack_id)  # recent opened stack
            if request.user.is_authenticated:
                current_stack.belongs_to = request.user

    except Stack.DoesNotExist:
        current_stack = Stack.objects.create(sid=stack_id,
                                             belongs_to=request.user if request.user.is_authenticated else None)
    return current_stack


def attach_current_stack_to_current_user(request, user):
    try:
        stack = Stack.objects.get(sid=open_stack(request).ID())
        if stack is not None:
            stack.belongs_to = user
            stack.save()
    except:
        print('no opened stack found to attach')


def merge_user_stacks(user):  # temporary approach
    try:
        # find all stacks belonging to the same user
        stacks_belonging_to_user = Stack.objects.filter(belongs_to=user)
        if not stacks_belonging_to_user or not stacks_belonging_to_user.count():
            return
        merged_stack = stacks_belonging_to_user[0]
        merged_stack_taken_products = TakenProduct.objects.filter(stack=merged_stack)

        if stacks_belonging_to_user is not None and stacks_belonging_to_user.count() > 1:
            trash = []
            # removing stacks directly will change the size of the stacks_belonging_to_user, and causes trouble
            # so i save the un wanted stacks in 'trash' and after that delete the items of trash one by one
            for stack in stacks_belonging_to_user:
                if stack.ID() != merged_stack.ID():
                    # if the item has no cost and isn't even a discounted free item, so its junk
                    if stack.belongs_to is None and stack.cost == 0 and stack.discounts < 100:
                        trash.append(stack)
                    else:
                        products_taken_by_user = TakenProduct.objects.filter(stack=stack)

                        for taken_product in products_taken_by_user:
                            taken_is_duplicate = False

                            similar_products_in_merged_stack = merged_stack_taken_products.filter(
                                product=taken_product.product
                            )  # FIXME: ISnt it only one taken product?
                            for possibly_duplicate in similar_products_in_merged_stack:
                                possibly_duplicate.quantity += taken_product.quantity
                                possibly_duplicate.save()
                                taken_product.delete()
                                taken_is_duplicate = True

                                if not taken_is_duplicate:
                                    taken_product.stack = merged_stack
                                    taken_product.save()

                        trash.append(stack)
            for stack in trash:
                stack.delete()

            # remove empty stacks:
            Stack.objects.filter(belongs_to=None, cost=0).delete()
    except Exception as ex:
        print('sth went wrong while trying to merge stacks: ' + ex.__str__())
