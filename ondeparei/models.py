from django.db import models
from ondeparei.util.strings import APP_NAME
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(User)
    bday = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=False, null=False, auto_now=True)
    # locale = models.OneToOneField('Locale', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.user.email)

    class Meta:
        app_label = APP_NAME
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Locale(models.Model):
    country = models.CharField(max_length=64, blank=False, null=False)
    state = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return '{} - {}'.format(self.state, self.country)

    class Meta:
        app_label = APP_NAME
        verbose_name = 'Locale'
        verbose_name_plural = 'Locales'


class Product(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    detail = models.ManyToManyField('Detail', blank=True, null=False)
    user = models.ForeignKey('UserModel', blank=False, null=False)
    timestamp = models.DateTimeField(blank=False, null=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = APP_NAME
        verbose_name = 'Produtct'
        verbose_name_plural = 'Products'


class Detail(models.Model):
    label = models.CharField(max_length=128, blank=False, null=False)
    value = models.CharField(max_length=128, blank=True, null=False)
    user = models.ForeignKey('UserModel', blank=False, null=False)
    timestamp = models.DateTimeField(blank=False, null=False, auto_now=True)

    def __str__(self):
        return self.label

    class Meta:
        app_label = APP_NAME
        verbose_name = 'Product Detail'
        verbose_name_plural = 'Product Details'


class Mark(models.Model):
    label = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(default='')
    product = models.ForeignKey('Product', blank=False, null=False)
    timestamp = models.DateTimeField(blank=False, null=False, auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.label, self.product.name)

    class Meta:
        app_label = APP_NAME
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'


# class DetailMark(models.Model):
#     label = models.CharField(max_length=128, blank=False, null=False)
#     value = models.CharField(max_length=128, blank=False, null=False)
#
#     class Meta:
#         app_label = APP_NAME
#         verbose_name = 'Mark Detail'
#         verbose_name_plural = 'Mark Details'


# class Observation(models.Model):
#     label = models.CharField(max_length=128, blank=False, null=False)
#     value = models.CharField(max_length=128, blank=False, null=False)
#
#     class Meta:
#         app_label = APP_NAME
#         verbose_name = 'Observation'
#         verbose_name_plural = 'Observations'
