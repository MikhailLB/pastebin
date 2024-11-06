from django.contrib.auth import get_user_model
from django.db import models
import random
import string
class PasteBin(models.Model):
    content = models.CharField(max_length=10485760)
    is_locked = models.BooleanField(default=True, verbose_name='СТАТУС')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    unique_hash = models.CharField(max_length=8, unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL
                               , null=True,
                               default=None)
    def save(self, *args, **kwargs):
        if not self.unique_hash:
            self.unique_hash = self.generate_unique_hash()
        super().save(*args, **kwargs)

    def generate_unique_hash(self):
        while True:
            # Генерация случайного хэша длиной 8 символов
            new_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            # Проверка уникальности хэша в базе данных
            if not PasteBin.objects.filter(unique_hash=new_hash).exists():
                return new_hash

    def __str__(self):
        return self.unique_hash