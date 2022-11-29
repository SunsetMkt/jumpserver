# Generated by Django 3.2.14 on 2022-11-28 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0112_gateway_to_asset'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounttemplate',
            options={'permissions': [('view_accounttemplatesecret', 'Can view asset account template secret'), ('change_accounttemplatesecret', 'Can change asset account template secret')], 'verbose_name': 'Account template'},
        ),
    ]