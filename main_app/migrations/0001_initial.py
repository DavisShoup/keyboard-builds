# Generated by Django 4.0.5 on 2022-07-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildname', models.CharField(max_length=100)),
                ('keyboard', models.CharField(max_length=100)),
                ('switch', models.CharField(max_length=100)),
                ('keycaps', models.CharField(max_length=100)),
            ],
        ),
    ]