# Generated by Django 2.2.1 on 2019-06-02 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190602_1911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'set_book_as_returned'),)},
        ),
    ]
