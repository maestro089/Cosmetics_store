# Generated by Django 4.0.6 on 2022-12-12 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Названеи товара')),
                ('photo', models.ImageField(upload_to='cosmetics/book/%Y/%m/%d/', verbose_name='Фотография товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации товара')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Производитель косметики')),
            ],
        ),
        migrations.CreateModel(
            name='types_cosmetics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Вид косметики')),
            ],
        ),
        migrations.CreateModel(
            name='comment_cosmetics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='Текст комментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('cosmetics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.book', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='store.types_cosmetics', verbose_name='Тип кометики'),
        ),
    ]
