# Generated by Django 4.0.5 on 2022-08-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('cate', models.CharField(max_length=100)),
                ('myfile', models.FileField(upload_to='MyFiles')),
                ('comments', models.TextField()),
            ],
        ),
    ]
