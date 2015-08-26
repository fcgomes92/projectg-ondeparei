# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=128)),
                ('value', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Product Detail',
                'verbose_name_plural': 'Product Details',
            },
        ),
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Locale',
                'verbose_name_plural': 'Locales',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=128)),
                ('description', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Mark',
                'verbose_name_plural': 'Marks',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('detail', models.ManyToManyField(to='ondeparei.Detail', blank=True)),
            ],
            options={
                'verbose_name': 'Produtct',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bday', models.DateField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AddField(
            model_name='mark',
            name='product',
            field=models.ForeignKey(to='ondeparei.Product'),
        ),
        migrations.AddField(
            model_name='detail',
            name='user',
            field=models.ForeignKey(to='ondeparei.UserModel'),
        ),
    ]
