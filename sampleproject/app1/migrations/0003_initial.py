# Generated by Django 4.2.7 on 2023-12-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0002_delete_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=50)),
                ('field2', models.CharField(max_length=50)),
            ],
        ),
    ]