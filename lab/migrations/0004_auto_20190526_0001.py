# Generated by Django 2.2 on 2019-05-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_auto_20190525_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooduse',
            name='meal_time',
            field=models.IntegerField(choices=[(1, 'breakfast'), (2, 'lunch'), (3, 'dinner'), (2, 'snacks')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='index',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
