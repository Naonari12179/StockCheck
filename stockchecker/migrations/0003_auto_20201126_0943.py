# Generated by Django 3.1.3 on 2020-11-26 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockchecker', '0002_auto_20201125_2323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='お菓子',
            options={'verbose_name': 'お菓子', 'verbose_name_plural': 'お菓子'},
        ),
        migrations.AlterModelOptions(
            name='お菓子fukuchi',
            options={'verbose_name': 'お菓子FUKUCHI', 'verbose_name_plural': 'お菓子FUKUCHI'},
        ),
        migrations.AlterModelOptions(
            name='お菓子uzawa',
            options={'verbose_name': 'お菓子UZAWA', 'verbose_name_plural': 'お菓子UZAWA'},
        ),
    ]
