# Generated by Django 3.1.3 on 2020-11-25 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockchecker', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='お菓子C',
            new_name='お菓子',
        ),
        migrations.RenameModel(
            old_name='お菓子B',
            new_name='お菓子FUKUCHI',
        ),
        migrations.RenameModel(
            old_name='お菓子A',
            new_name='お菓子UZAWA',
        ),
        migrations.CreateModel(
            name='飲料',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockchecker.categorys')),
            ],
            options={
                'verbose_name': '飲料',
                'verbose_name_plural': '飲料',
            },
        ),
        migrations.CreateModel(
            name='洋日配',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('商品名', models.CharField(max_length=200)),
                ('dis_date', models.DateTimeField(verbose_name='賞味')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='stockchecker.categorys')),
            ],
            options={
                'verbose_name': '洋日配',
                'verbose_name_plural': '洋日配',
            },
        ),
    ]
