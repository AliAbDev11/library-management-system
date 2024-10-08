# Generated by Django 5.1.1 on 2024-09-12 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('book_img', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('author_img', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rental_bookprice', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('retal_period', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('rental', 'rental'), ('sold', 'sold')], max_length=50, null=True)),
                ('categorie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lms_app.categorie')),
            ],
        ),
    ]
