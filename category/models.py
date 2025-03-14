from django.db import models
from django.urls import reverse

# TODO: Maybe Create description page for each category, so that we can use its sitemap instance

# category model for classifying your products
class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True, verbose_name="نام دسته")
    name_fa = models.CharField(max_length=30, blank=False, unique=True, verbose_name="فارسی نام دسته")
    slug = models.SlugField(max_length=30, unique=True, verbose_name="اسلاگ")
    description = models.TextField(max_length=256, blank=True, verbose_name="توضیحات")
    icon = models.ImageField(upload_to='photos/categories/', blank=True, verbose_name="آیکون") # optional field
    branch_of = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='زیرشاخه دسته بندی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به روز رسانی")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def url(self):
        return reverse('filtered_by_category', args=[self.slug])  # or-> '/store/' + self.slug + '/'

    def __str__(self) -> str:
        return self.name_fa

    def get_absolute_url(self):
        return self.url()