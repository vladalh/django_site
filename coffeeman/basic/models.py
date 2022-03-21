from django.db import models


class Review(models.Model):
    name = models.CharField('Введите имя', max_length=25)
    email = models.EmailField('Введите адрес электронной почты')
    comments = models.TextField('Напишите свой отзыв', max_length=150)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
