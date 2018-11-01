# Generated by Django 2.1.1 on 2018-10-11 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20181009_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='polls',
            name='readed_num',
        ),
        migrations.AlterField(
            model_name='polls',
            name='polls_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.PollsType'),
        ),
        migrations.AddField(
            model_name='readnum',
            name='polls',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Polls'),
        ),
    ]