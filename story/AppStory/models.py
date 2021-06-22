from django.db import models
from .choices import CHOICES_TYPE
from django.core.validators import MaxValueValidator
# Create your models here.


class Project(models.Model):
    name = models.CharField('Название проекта', max_length=25)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name


class Story(models.Model):
    preview = models.ImageField('Превью', upload_to='media/')
    start_date = models.DateTimeField("Начала актуальности")
    end_date = models.DateTimeField("Конец актуальности")
    add_date = models.DateTimeField(auto_now_add=True)
    order_num = models.IntegerField("Приоритет")
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING, verbose_name="Проект")

    def __str__(self):
        return f'{self.start_date} | {self.project_id}'


class StoryFile(models.Model):
    more_detailed_url = models.URLField("Подробнее")
    more_detailed_text = models.TextField("Описание")
    content_type = models.CharField("Тип", max_length=100, choices=CHOICES_TYPE)
    content_url = models.URLField("Контент")
    duration = models.IntegerField("Длина в секундах", validators=[MaxValueValidator(100)])
    story_id = models.ForeignKey(Story, on_delete=models.DO_NOTHING, verbose_name='Сторис')
    start_date = models.DateTimeField("Начала актуальности")
    end_date = models.DateTimeField("Конец актуальности")

    def __str__(self):
        return self.start_date


class UserStoryFile(models.Model):
    story_file = models.ForeignKey(StoryFile, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    is_watched = models.BooleanField(default=False)
    watch_date = models.DateTimeField(null=True, blank=True)


class User(models.Model):
    subs_id = models.IntegerField(primary_key=True)