# Generated by Django 3.0.5 on 2020-04-10 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('bank', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='bank.Bank')),
            ],
        ),
    ]
