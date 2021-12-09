# Generated by Django 3.2.6 on 2021-11-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0002_videos_transcript'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
                ('transcript', models.TextField(blank=True, null=True)),
                ('audio', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
    ]
