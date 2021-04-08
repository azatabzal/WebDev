# Generated by Django 3.1.7 on 2021-04-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('is_active', models.BooleanField(verbose_name='Есть в наличии')),
            ],
        ),
    ]
