# Generated by Django 2.1.2 on 2018-10-17 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20181016_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='polls_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.PollsType'),
        ),
    ]