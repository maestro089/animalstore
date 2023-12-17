from django.db import models
from django.contrib.auth.models import User

from store.models import Product


class Cart(models.Model):
    object = None
    title = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Покупатель"
    )
    quentity = models.IntegerField(verbose_name="Количество", null=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины пользователей"


class Order(models.Model):
    STATUS_CHOICES = (
        ("processed", "Обрабатывается"),
        ("sent", "Отправлен"),
        ("delivered", "Доставлен"),
    )
    customer = models.ForeignKey(
        User,
        related_name="Покупатель",
        on_delete=models.CASCADE,
        verbose_name="Покупатель",
    )
    products = models.ManyToManyField(Product, verbose_name="Товар", blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="processed",
        verbose_name="Статус",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.products} - {self.created}"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")
    quantity = models.PositiveSmallIntegerField(verbose_name="Количество товара")

    def __str__(self):
        return f"{self.product}"
