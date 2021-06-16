# Generated by Django 3.2.1 on 2021-06-14 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('important', models.BooleanField(default=False, verbose_name='مهم')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('datecomplete', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ کامل شدن')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'تودو',
                'verbose_name_plural': 'تودوها',
            },
        ),
    ]