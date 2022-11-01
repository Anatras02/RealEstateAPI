# Generated by Django 4.1.3 on 2022-11-01 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comune',
            fields=[
                ('codice_istat', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Regione',
            fields=[
                ('codice_istat', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Quartiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('comune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indirizzo.comune')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('codice_istat', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('regione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indirizzo.regione')),
            ],
        ),
        migrations.CreateModel(
            name='Indirizzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('via', models.CharField(max_length=50)),
                ('civico', models.CharField(max_length=10)),
                ('quartiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indirizzo.quartiere')),
            ],
        ),
        migrations.AddField(
            model_name='comune',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indirizzo.provincia'),
        ),
    ]
