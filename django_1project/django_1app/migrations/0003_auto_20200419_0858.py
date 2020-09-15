# Generated by Django 3.0.1 on 2020-04-19 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_1app', '0002_aiport'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aiport',
            new_name='Airport',
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='django_1app.Airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='django_1app.Airport')),
            ],
        ),
    ]
