# Generated by Django 3.2.3 on 2021-05-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_fileupload_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotesApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20)),
                ('quote_type', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=20)),
                ('quote', models.TextField(max_length=150)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
