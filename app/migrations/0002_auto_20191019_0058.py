# Generated by Django 2.1.13 on 2019-10-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelname',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image/'),
        ),
        migrations.AddField(
            model_name='modelname',
            name='tiile',
            field=models.CharField(default='作品标题', max_length=50),
        ),
    ]