# Generated by Django 3.2 on 2021-04-21 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Craft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo_capacity', models.BigIntegerField()),
                ('consumables', models.CharField(max_length=100)),
                ('cost_in_credits', models.BigIntegerField()),
                ('crew', models.IntegerField()),
                ('length', models.DecimalField(decimal_places=10, max_digits=20)),
                ('manufacturer', models.CharField(max_length=500)),
                ('max_atmosphering_speed', models.IntegerField()),
                ('model', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('passengers', models.IntegerField()),
                ('hyperdrive_rating', models.FloatField()),
                ('url', models.CharField(default=None, max_length=100)),
                ('vehicle_class', models.CharField(max_length=100)),
                ('starship_class', models.CharField(max_length=100)),
                ('MGLT', models.CharField(max_length=100)),
                ('sell_price', models.IntegerField()),
                ('condition', models.CharField(choices=[('Bucket', 'Bucket'), ('Fair', 'Fair'), ('Good', 'Good'), ('Excellent', 'Excellent'), ('Like New', 'Like New')], default='Good', max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('mileage', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('image', models.CharField(blank=True, max_length=100)),
                ('badges', models.ManyToManyField(to='main_app.Badge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('craft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.craft')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('craft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.craft')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
