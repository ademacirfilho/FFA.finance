# Generated by Django 5.1.3 on 2024-11-25 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaFFA', '0002_pagamento_alter_transacao_tipopagamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='transacao',
            name='categoriaNome',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sistemaFFA.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transacao',
            name='contatoNome',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sistemaFFA.contato'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemaFFA.tipocategoria'),
        ),
    ]
