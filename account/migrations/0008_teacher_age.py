# Generated by Django 3.2.6 on 2021-12-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20211111_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.CharField(default=12, max_length=60),
            preserve_default=False,
        ),
    ]
