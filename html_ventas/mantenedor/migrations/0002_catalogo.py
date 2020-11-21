# Generated by Django 3.1.2 on 2020-11-11 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('precio', models.CharField(default='', max_length=20)),
                ('stock', models.CharField(default='', max_length=100)),
                ('imgCatalogo', models.ImageField(default='null', upload_to='fotosPostres')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'catalogo',
            },
        ),
    ]