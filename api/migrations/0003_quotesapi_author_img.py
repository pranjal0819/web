# Generated by Django 3.2.3 on 2021-05-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210525_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotesapi',
            name='author_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
