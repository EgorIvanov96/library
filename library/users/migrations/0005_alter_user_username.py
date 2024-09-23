# Generated by Django 5.1.1 on 2024-09-23 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options_remove_user_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Укажите имя пользователя', max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+\\Z', 'Поле username содержит недопустимые символы')], verbose_name='Имя пользователя'),
        ),
    ]
