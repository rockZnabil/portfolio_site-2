# Generated by Django 2.0.3 on 2018-09-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_name', models.CharField(help_text='Publication name', max_length=200)),
                ('date_of_publication', models.DateField()),
            ],
        ),
    ]
