# Generated by Django 2.1.3 on 2018-11-16 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front_end', '0007_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_name',
            new_name='book_name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publication_url',
            new_name='book_url',
        ),
    ]