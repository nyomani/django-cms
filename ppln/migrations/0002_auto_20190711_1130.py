# Generated by Django 2.1 on 2019-07-11 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ppln', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='election_type',
            field=models.ForeignKey(default=1, help_text='Election Types', on_delete=django.db.models.deletion.CASCADE, to='ppln.ElectionType'),
        ),
    ]