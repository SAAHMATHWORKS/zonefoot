# Generated by Django 3.2.8 on 2022-08-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0003_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='info1',
        ),
        migrations.RemoveField(
            model_name='info',
            name='info2',
        ),
        migrations.AddField(
            model_name='info',
            name='info',
            field=models.CharField(default='Finale ce vendredi', max_length=100),
            preserve_default=False,
        ),
    ]
