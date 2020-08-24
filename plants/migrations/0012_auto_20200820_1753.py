# Generated by Django 3.0.9 on 2020-08-20 15:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plants', '0011_auto_20200818_2130'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='plant',
            unique_together={('name', 'owner')},
        ),
    ]
