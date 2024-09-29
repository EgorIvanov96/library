from django.db import models

from users.models import User


class Books(models.Model):
    """Класс книжек."""
    name_book = models.CharField(
        max_length=150,
        verbose_name='Название книги',
        help_text='Введите название книги',
        unique=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор книги',
        help_text='Введите автора книги'
    )
    date_publication = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'книги'
        ordering = ['name_book',]

    def __str__(self):
        return self.name_book
