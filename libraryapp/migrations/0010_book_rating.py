# Generated by Django 2.2.1 on 2020-02-29 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0009_libranian_normaluser_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1),
        ),
    ]
