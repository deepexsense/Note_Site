# Generated by Django 2.0 on 2019-05-06 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0002_note_open_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['date']},
        ),
    ]
