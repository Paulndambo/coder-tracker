# Generated by Django 4.0.2 on 2022-02-04 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Week',
        ),
        migrations.AddField(
            model_name='activity',
            name='week',
            field=models.CharField(default=1, max_length=200),
        ),
    ]