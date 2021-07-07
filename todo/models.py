from django.db import models
from account.models import User
from django.urls import reverse
from random import randint


class ToDo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    memo = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    important = models.BooleanField(default=False, verbose_name='مهم')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    datecomplete = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ کامل شدن')

    class Meta:
        verbose_name = 'تودو'
        verbose_name_plural = 'تودوها'

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            is_unique = False
            while not is_unique:
                id = randint(1000000000000000000, 1999999999999999999) # 19 digits: 1, random 18 digits
                is_unique = not ToDo.objects.filter(id=id).exists()
            self.id = id
        super(ToDo, self).save()