# Generated by Django 4.0.6 on 2022-12-12 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_book_cosmetics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manufacturer',
            new_name='Manufacturers',
        ),
        migrations.AddField(
            model_name='cosmetics',
            name='Manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.manufacturers', verbose_name='Производитель кометики'),
        ),
    ]
