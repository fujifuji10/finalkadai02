# Generated by Django 5.0.6 on 2024-07-17 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_alter_housingpictures_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='size',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
