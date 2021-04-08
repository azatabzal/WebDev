from django.db import models

class Product(models.Model):
	name = models.CharField('Имя', max_length=50)
	price = models.FloatField('Цена')
	description = models.TextField('Описание')
	count = models.IntegerField('Количество')
	is_active = models.BooleanField('Есть в наличии')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

class Category(models.Model):
    name = models.CharField('Имя', max_length = 50)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'