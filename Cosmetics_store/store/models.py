from django.db import models
from django.contrib.auth.models import User

class types_cosmetics (models.Model):
    object = None
    title = models.CharField(max_length=255, blank = True, verbose_name="Вид косметики")

    def __str__(self):
        return self.title

class Manufacturers (models.Model):
    object = None
    title = models.CharField(max_length=255, blank = True, verbose_name="Производитель косметики")

    def __str__(self):
        return self.title


class cosmetics (models.Model):
    objects = None
    title = models.CharField(max_length=255, verbose_name = "Названеи товара")
    photo = models.ImageField(upload_to="cosmetics/book/%Y/%m/%d/", verbose_name = "Фотография товара")
    description = models.TextField(blank=True, verbose_name = "Описание товара")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = "Дата публикации товара")
    price = models.FloatField(verbose_name = "Цена")
    type = models.ForeignKey(types_cosmetics, null = False, blank = True, verbose_name = "Тип кометики",on_delete = models.CASCADE)
    Manufacturer = models.ForeignKey(Manufacturers, null = True, blank = True, verbose_name = "Производитель кометики",on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/product/{self.id}'


class comment_cosmetics(models.Model):
        object = None
        text = models.TextField(blank=True, verbose_name = "Текст комментария")
        author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
        cosmetics = models.ForeignKey(cosmetics, on_delete=models.CASCADE, verbose_name='Товар')
