# Generated by Django 3.0.4 on 2020-04-26 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phase', '0001_initial'),
        ('annex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annex',
            name='annex_phase',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='phase.AnnexPhase', verbose_name='文件类型'),
        ),
    ]
