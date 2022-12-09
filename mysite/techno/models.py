from django.db import models
from django.urls import reverse


class Techno(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='static/media/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('goods', kwargs={'goods_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
