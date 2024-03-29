# Generated by Django 4.2.7 on 2023-12-06 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calgen", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CalenderWeek",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                ("number", models.IntegerField()),
                ("start", models.DateField()),
                ("end", models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="week",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="calgen.calenderweek",
            ),
        ),
    ]
