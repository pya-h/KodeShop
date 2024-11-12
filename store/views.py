import json

from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from .models import Product, Review, Gallery
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from math import ceil as number_ceil


MAX_ITEMS_IN_PAGE = 30
MAX_PAGINATION_BUTTON_RANGE = 3

def store(request, category_filter=None):
    max_price = min_price = 0
    category_fa = None
    try:
        page = int(request.GET.get('page', 1))
        if page < 1:
            raise ValueError('page not positive!')
    except ValueError:
        page = 1
    try:
        items_count_limit = int(request.GET.get('items', MAX_ITEMS_IN_PAGE))
        if items_count_limit < 1:
            raise ValueError('limit not positive!')
    except ValueError:
        items_count_limit = MAX_ITEMS_IN_PAGE

    filters = Q()

    try:

        if category_filter:
            obj_expected_categories = get_object_or_404(Category, slug=category_filter)
            category_fa = obj_expected_categories.name_fa
            if obj_expected_categories:
                filters &= Q(category=obj_expected_categories)

        if request.method == "POST":
            try:
                min_price = int(request.POST["min_price"])
            except:
                min_price = 0

            try:
                max_price = int(request.POST["max_price"])
            except:
                max_price = 0

            if min_price > 0:
                filters &= Q(price__gte=min_price)
            if max_price > 0:
                filters &= Q(price__lte=max_price)

    except Exception as ex:
        print(ex.__str__())
        products = []

    total_items_count = Product.objects.count()
    page_count = number_ceil(total_items_count / items_count_limit)
    if page > page_count:
        page = page_count
    products = Product.objects.filter(filters)[(page-1)*items_count_limit:page*items_count_limit]
    context = {
        'products': products,
        'products_count': products.count() if products else 0,
        'current_category': category_fa,
        'category_filter': category_filter,
        'max_price': max_price,
        'min_price': min_price,
        'page': page,
        'items_limit': min(items_count_limit, total_items_count),
        'page_count': page_count,
        'pagination_range': MAX_PAGINATION_BUTTON_RANGE,
    }

    return render(request, 'store/store.html', context)


def product(request, category_filter, product_slug=None):
    context = dict()
    try:
        this_product = Product.objects.get(slug=product_slug, category__slug=category_filter)
        reviews = Review.objects.filter(product=this_product, status=True)
        gallery = Gallery.objects.filter(product=this_product)
        context = {
            'this_product': this_product,
            'reviews': reviews,
            'gallery': gallery,
        }
    except Exception as ex:
        # handle this seriously
        raise ex

    return render(request, 'store/product.html', context)


@login_required(login_url='login')
def post_review(request, product_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                old_review = Review.objects.get(user__id=request.user.id, product__id=product_id)
                form = ReviewForm(request.POST, instance=old_review)  # instance=review parameter will prevent from
                # django from creating new review, and it will replace existing one
                form.save()
                messages.info(request, "نظر شما به روز رسانی شد.")
            except Review.DoesNotExist:
                form = ReviewForm(request.POST)
                if form.is_valid():
                    try:
                        product_to_be_reviewed = Product.objects.get(id=product_id)
                        new_review = Review(product=product_to_be_reviewed, user=request.user,
                                            comment=form.cleaned_data['comment'], rating=form.cleaned_data['rating'],
                                            ip=request.META.get('REMOTE_ADDR'))
                        # validate form and ip first
                        new_review.save()
                        messages.success(request, 'نظر شما ثبت شد.')
                    except Product.DoesNotExist:
                        messages.error(request, 'متاسفانه چنین کالایی وجود ندارد. در نتیجه نظر شما را نمی توانیم ثبت '
                                                'کنیم.')
    else:
        messages.error(request, 'برای ارسال نظر ابتدا باید وارد حساب کاربری خود شوید.')
    return redirect(request.META.get('HTTP_REFERER'))