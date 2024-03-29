# Generated by Django 3.2.6 on 2022-07-09 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_book_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(default='', max_length=50, verbose_name='书籍id')),
                ('title', models.CharField(default='', max_length=50, verbose_name='书籍名称')),
                ('store', models.CharField(default='', max_length=50, verbose_name='所属商店')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='价格')),
                ('status', models.CharField(default='0', max_length=5, verbose_name='书籍状态')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2022, 7, 9, 23, 17, 53, 797616), verbose_name='创建时间')),
                ('updata_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('num', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='库存')),
            ],
            options={
                'db_table': 'tb_book_info',
            },
        ),
    ]
