# Generated by Django 5.0.3 on 2024-04-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homework5app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_add',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=999999.99, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='value',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
