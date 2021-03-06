# Generated by Django 3.2.4 on 2021-06-22 05:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(upload_to='media/', verbose_name='Превью')),
                ('start_date', models.DateTimeField(verbose_name='Начала актуальности')),
                ('end_date', models.DateTimeField(verbose_name='Конец актуальности')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('order_num', models.IntegerField(verbose_name='Приоритет')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AppStory.project', verbose_name='Проект')),
            ],
        ),
        migrations.CreateModel(
            name='StoryFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_detailed_url', models.URLField(verbose_name='Подробнее')),
                ('more_detailed_text', models.TextField(verbose_name='Описание')),
                ('content_type', models.CharField(choices=[(1, 'IMG'), (2, 'VIDEO')], max_length=100, verbose_name='Тип')),
                ('content_url', models.URLField(verbose_name='Контент')),
                ('duration', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Длина в секундах')),
                ('start_date', models.DateTimeField(verbose_name='Начала актуальности')),
                ('end_date', models.DateTimeField(verbose_name='Конец актуальности')),
                ('story_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AppStory.story', verbose_name='Сторис')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('subs_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserStoryFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_watched', models.BooleanField(default=False)),
                ('watch_date', models.DateTimeField(blank=True, null=True)),
                ('story_file', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AppStory.storyfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AppStory.user')),
            ],
        ),
    ]
