# Generated by Django 4.1.5 on 2023-02-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
