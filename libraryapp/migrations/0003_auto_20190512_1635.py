# Generated by Django 2.2 on 2019-05-12 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraryapp', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('barcode', models.CharField(max_length=100)),
                ('author', models.ManyToManyField(to='libraryapp.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='bookcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('duration', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(upload_to='program')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='publisher')),
                ('website', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='Admin',
            new_name='Libranian',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('semester', models.CharField(choices=[('semester 1', 'SEMESTER I'), ('semester 2', 'SEMESTER II'), ('semester 3', 'SEMESTER III'), ('semester 4', 'SEMESTER IV'), ('semester 5', 'SEMESTER V')], max_length=100)),
                ('section', models.CharField(choices=[('section A', 'section A'), ('section B', 'section B'), ('section C', 'section C'), ('section D', 'section D')], max_length=100)),
                ('image', models.ImageField(upload_to='student')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Program')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ManyToManyField(to='libraryapp.Book')),
                ('libranian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Libranian')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ManyToManyField(to='libraryapp.Book')),
                ('libranian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Libranian')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='libraryapp.BookCategory'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Publisher'),
        ),
    ]
