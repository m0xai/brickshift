# Generated by Django 4.2.7 on 2023-11-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeekPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_week', models.IntegerField()),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]