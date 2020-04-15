# Generated by Django 3.0.4 on 2020-04-15 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='books.Tag'),
        ),
    ]