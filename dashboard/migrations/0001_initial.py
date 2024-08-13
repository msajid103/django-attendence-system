# Generated by Django 4.2.4 on 2023-09-05 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('roll_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('allow_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField()),
                ('exit_time', models.DateTimeField()),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.student')),
            ],
        ),
    ]
