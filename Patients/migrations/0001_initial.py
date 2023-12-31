# Generated by Django 4.2.3 on 2023-09-03 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('category', models.CharField(choices=[('Heart Patients', 'Heart Patients'), ('Liver Patients', 'Liver Patients')], max_length=50)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='Doctors.doctor')),
            ],
        ),
    ]
