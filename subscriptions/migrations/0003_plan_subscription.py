# Generated by Django 3.2 on 2022-02-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_rename_line13_plan_line3'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='subscription',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
