# Generated by Django 3.2.14 on 2022-11-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0016_auto_20221125_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectiontoken',
            name='connect_method',
            field=models.CharField(default='web_ui', max_length=32, verbose_name='Connect method'),
            preserve_default=False,
        ),
    ]