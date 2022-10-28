# Generated by Django 4.0.5 on 2022-10-25 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_photos_albumid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='albumId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='base.album'),
        ),
    ]
