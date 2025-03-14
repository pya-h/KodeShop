from os.path import join
from django.db import models
from category.models import Category
from django.urls import reverse
from user.models import User
from django.db.models import Avg, Count


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False, verbose_name="نام به انگلیسی")
    name_fa = models.CharField(max_length=64, unique=True, blank=False, verbose_name="نام")
    slug = models.SlugField(max_length=64, unique=True, verbose_name="اسلاگ")
    description = models.TextField(max_length=1024, blank=True, verbose_name="مشخصات")
    price = models.IntegerField(verbose_name="قیمت")
    stock = models.IntegerField(verbose_name="موجودی")
    available = models.BooleanField(default=True, verbose_name="در دسترس؟")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد این محصول")
    modified = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرزین تغییر اطلاعات")
    discount = models.IntegerField(default=0, verbose_name="تخفیف")  # discount in percentage
    # below line delete all products associated when the category deletes!! expected?
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی")
    image = models.ImageField(upload_to='photos/products', verbose_name="تصویر")

    class Meta:
        verbose_name = "کالا"
        verbose_name_plural = "کالا ها"

    # this is IMPORTANT -> remove image from here and add use default variation image

    def url(self):
        return reverse('single_product', args=[self.category.slug, self.slug])

    def get_absolute_url(self):
        return self.url()

    def ID(self):
        return self.id

    def __str__(self):
        return self.name_fa
        # return self.name_fa


    def format_rating(self):
        reviews = Review.objects.filter(product=self, status=True).aggregate(average_rating=Avg('rating'),
                                                                             count=Count('id'))
        if reviews['count']:
            return f'{float(reviews["average_rating"])}/5.0 [{int(reviews["count"])}]'
        return "-"

    def rating(self):
        try:
            return Review.objects.filter(product=self, status=True).aggregate(average_rating=Avg('rating'))[
                'average_rating']
        except Exception as ex:
            print("Something went wrong while calculating product rating because: ", ex)
        return None


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, verbose_name="کالای مرتبط")
    image = models.ImageField(upload_to='photos/products', verbose_name="تصویر")

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری"

    def __str__(self):
        return self.product.__str__()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="کالای مرتبط")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    comment = models.TextField(max_length=500, blank=True, verbose_name="نظر")
    rating = models.FloatField(verbose_name="امتیاز")
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد نظر")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="به روز رسانی اطلاعات نظز")

    class Meta:
        verbose_name = 'نظر کاربران'
        verbose_name_plural = 'نظرات کاربران'

    def __str__(self):
        return f'{self.user.fname}: {self.comment}'
