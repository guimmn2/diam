# Generated by Django 4.1.7 on 2023-03-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0005_alter_aluno_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='avatar',
            field=models.ImageField(default='/votacao/static/media/user.png', upload_to='static/media'),
        ),
    ]
