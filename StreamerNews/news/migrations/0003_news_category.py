# Generated by Django 5.0 on 2023-12-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0002_alter_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(blank=True,
                                   choices=[('game', 'game'), ('irl', 'irl'),
                                            ('event', 'good')], max_length=50,
                                   null=True),
        ),
    ]
