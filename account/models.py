from django.db import models
from django.contrib.auth.models import AbstractUser
import os
import datetime


# Create your models here.

## Get the file name and extension.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

## Change the file name and upload it.
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    now = datetime.datetime.now()
    final_name = f"{instance.id}-{instance.username}-{now:%H-%M-%S}{ext}"
    return f"users/User: {instance.username}/{now:%Y-%m-%d}/{final_name}"

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True, verbose_name='تصویر')