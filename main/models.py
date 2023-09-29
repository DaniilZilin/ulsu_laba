from django.db import models


class GovernmentEmployee(models.Model):
    id = models.IntegerField('ID', primary_key=True)
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    surname = models.CharField('Отчество', max_length=255)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Госслужащий'
        verbose_name_plural = 'Госслужащие'


class Administration(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Администрация'
        verbose_name_plural = 'Администрация'


class Question(models.Model):
    addressee = models.ForeignKey(Administration, on_delete=models.CASCADE, verbose_name='PK чиновника')
    name = models.CharField('Полное имя', max_length=255)
    question = models.CharField('Вопрос', max_length=255)
    email = models.EmailField('E-mail', max_length=255)
    text_of_question = models.TextField('Текст вопроса')
    phone_number = models.CharField('Номер телефона', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


