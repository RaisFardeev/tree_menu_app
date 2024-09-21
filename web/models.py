from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(verbose_name='Название меню', max_length=100, unique=True)
    description = models.TextField(verbose_name='Описание', max_length=300, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(verbose_name='Название пункта меню', max_length=50, unique=True)
    description = models.TextField(verbose_name='Описание', max_length=300, blank=True)
    url = models.CharField(verbose_name='URL', max_length=50, blank=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def save(self, *args, **kwargs):
        if self.named_url:
            try:
                self.url = reverse(self.named_url)
            except NoReverseMatch:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
