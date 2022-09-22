from django.db import models

from usersapp.models import User


class Project(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)
    repo = models.URLField(verbose_name='Репозиторий', blank=True)
    users = models.ManyToManyField(User, verbose_name='Пользователи')

    def __str__(self):
        return f'({self.id}) {self.name}'

class ToDo(models.Model):
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE)
    subject = models.TextField(verbose_name='Текст', blank=True, null=False)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Cоздана', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлена', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активна', default=True)




