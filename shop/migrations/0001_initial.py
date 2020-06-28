# Generated by Django 3.0.6 on 2020-06-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('stock', models.SmallIntegerField()),
                ('pclass', models.CharField(max_length=50)),
                ('pdescribe', models.CharField(max_length=500)),
            ],
        ),
    ]
