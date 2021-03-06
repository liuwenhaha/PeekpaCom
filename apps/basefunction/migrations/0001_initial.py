# Generated by Django 2.1.15 on 2020-05-20 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('show_name', models.CharField(max_length=30)),
                ('url_path', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('show_page', models.PositiveIntegerField(choices=[(0, '首页'), (1, 'CMS'), (2, '论坛')], default=0)),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除'), (2, '草稿')], default=2)),
            ],
        ),
    ]
