from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    object = None
    title = models.CharField(
        max_length=255, blank=True, verbose_name="Название категории"
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name="Название")
    photo = models.ImageField(
        upload_to="photo/product/%Y/%m/%d/", verbose_name="Фотография"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации"
    )
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    price = models.FloatField(verbose_name="Цена")
    genre = models.ForeignKey(
        Category,
        null=False,
        blank=True,
        verbose_name="Кагория",
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return f"/{self.id}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class CommentsProduct(models.Model):
    object = None
    text = models.TextField(blank=True, verbose_name="Текст комментария")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор комментария"
    )
    comment_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="ТОвар"
    )
    is_publishe = models.BooleanField(
        default=True, verbose_name="Публикация комметария"
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.comment_product.title
