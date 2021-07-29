# Generated by Django 3.2.5 on 2021-07-26 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=200)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=100)),
                ('date_receita', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
