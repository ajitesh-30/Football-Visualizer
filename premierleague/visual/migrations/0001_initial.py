# Generated by Django 2.0.2 on 2019-11-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('league', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('current_club', models.CharField(max_length=100)),
                ('minutes_played', models.IntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('appearances', models.IntegerField(max_length=100)),
                ('goals_overall', models.IntegerField(default=0)),
                ('goals_home', models.IntegerField(default=0)),
                ('goals_away', models.IntegerField(default=0)),
                ('assists_overall', models.IntegerField(default=0)),
                ('clean_sheets_overall', models.IntegerField(default=0)),
                ('yellow_cards_overall', models.IntegerField(default=0)),
                ('red_cards_overall', models.IntegerField(default=0)),
            ],
        ),
    ]