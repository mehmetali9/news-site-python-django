# Generated by Django 4.0 on 2022-01-03 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Başlık')),
                ('body', models.TextField(verbose_name='Metin')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Tarih')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser', verbose_name='Yazar')),
            ],
        ),
    ]
