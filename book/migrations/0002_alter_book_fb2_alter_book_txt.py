# Generated by Django 4.2.1 on 2023-05-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='fb2',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='txt',
            field=models.FileField(upload_to=''),
        ),
    ]
