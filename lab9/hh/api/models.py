from django.db import models

class company(models.Model):
	name = models.CharField('Имя', max_length=50)
	description = models.TextField('Описание')
	city = models.CharField('Город', max_length=50)
	address = models.TextField('Адрес')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Компания'
		verbose_name_plural = 'Компании'

class vacancy(models.Model):
	name = models.CharField('Имя', max_length=50)
	description = models.TextField('Описание')
	salary = models.FloatField('Зарплата')
	company = models.ForeignKey(company, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Вакансия'
		verbose_name_plural = 'Вакансии'