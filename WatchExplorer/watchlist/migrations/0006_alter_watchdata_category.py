# Generated by Django 4.2.1 on 2023-05-30 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0005_alter_watchdata_options_watchdata_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchdata',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='watchlist.category'),
        ),
    ]
