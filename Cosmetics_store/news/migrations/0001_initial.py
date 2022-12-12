# Generated by Django 4.0.6 on 2022-11-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='News name')),
                ('photo', models.ImageField(upload_to='photo/book/%Y/%m/%d/', verbose_name='News photo')),
                ('text', models.TextField(blank=True, verbose_name='Text')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Date publisher')),
                ('is_published', models.BooleanField(default=True, verbose_name='Publisher')),
            ],
        ),
    ]