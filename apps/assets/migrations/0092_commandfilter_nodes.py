# Generated by Django 3.2.15 on 2022-10-09 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0091_auto_20220629_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandfilter',
            name='nodes',
            field=models.ManyToManyField(blank=True, related_name='cmd_filters', to='assets.Node', verbose_name='Nodes'),
        ),
    ]