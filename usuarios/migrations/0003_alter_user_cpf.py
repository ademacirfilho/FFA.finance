# Generated by Django 5.1.3 on 2025-02-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_user_avatar_user_cpf_user_telefone_delete_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
