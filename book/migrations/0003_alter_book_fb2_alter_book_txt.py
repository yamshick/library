# Generated by Django 4.2.1 on 2023-05-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_fb2_alter_book_txt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='fb2',
            field=models.FileField(upload_to='book/fb2'),
        ),
        migrations.AlterField(
            model_name='book',
            name='txt',
            field=models.FileField(upload_to='book/txt'),
        ),
    ]
