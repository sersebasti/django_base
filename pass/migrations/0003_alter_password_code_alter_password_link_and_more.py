# Generated by Django 4.2.6 on 2023-12-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0002_rename_useranme_password_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='note',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
