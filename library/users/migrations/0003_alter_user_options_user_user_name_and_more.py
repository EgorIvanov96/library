# Generated by Django 5.1.1 on 2024-09-20 11:19

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_remove_user_user_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['user_name'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default=0, help_text='Укажите имя пользователя', max_length=150, verbose_name='Имя пользователя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
