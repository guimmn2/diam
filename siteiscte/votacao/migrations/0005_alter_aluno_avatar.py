# Generated by Django 4.1.7 on 2023-03-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0004_aluno_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='avatar',
            field=models.CharField(default='votacao/static/media/user.png', max_length=100),
        ),
    ]
