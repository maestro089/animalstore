from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name="Название новости")
    photo = models.ImageField(upload_to="news/%Y/%m/%d/", verbose_name="Фотография")
    text = models.TextField(blank=True, verbose_name="Текст")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикация"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Comment(models.Model):
    object = None
    text = models.TextField(blank=True, verbose_name="Текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    news_id = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новость")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.news_id.title


class Images(models.Model):
    object = None
    news_id = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новость")
    path_img = models.TextField(verbose_name="Путь к Фотографии")

    class Meta:
        verbose_name = "Фотография новости"
        verbose_name_plural = "Фотография новостей"
