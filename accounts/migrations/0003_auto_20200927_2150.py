# Generated by Django 3.1.1 on 2020-09-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200927_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='الاسم :'),
        ),
        migrations.AddField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name=' سعر الكشف '),
        ),
        migrations.AddField(
            model_name='profile',
            name='who_i',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name=' من انا : '),
        ),
    ]
