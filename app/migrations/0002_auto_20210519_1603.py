# Generated by Django 3.2.3 on 2021-05-19 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='first_vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_vote', to='app.namemaster'),
        ),
        migrations.AlterField(
            model_name='result',
            name='second_vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_vote', to='app.namemaster'),
        ),
        migrations.AlterField(
            model_name='result',
            name='third_vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_vote', to='app.namemaster'),
        ),
        migrations.AlterField(
            model_name='result',
            name='voter_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter_name', to='app.namemaster'),
        ),
    ]
