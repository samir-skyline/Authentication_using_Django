# Generated by Django 5.0.6 on 2024-07-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_loginmodel_email_alter_studentmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='password',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='age',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
