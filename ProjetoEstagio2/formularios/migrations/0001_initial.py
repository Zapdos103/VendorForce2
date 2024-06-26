# Generated by Django 5.0.3 on 2024-03-31 22:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('topico', models.CharField(max_length=120)),
                ('qtd_questoes', models.IntegerField()),
                ('tempo', models.IntegerField(help_text='Duração do teste em minutos')),
                ('qtd_acertos', models.IntegerField(help_text='Pontuação realizada pelo usuário %')),
                ('texto', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=120)),
                ('data_criacao', models.DateField(default=datetime.date.today)),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.formulario')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=120)),
                ('acerto', models.BooleanField(default=False)),
                ('data_criacao', models.DateField(default=datetime.date.today)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.questao')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default=None, max_length=200)),
                ('pontuacao', models.FloatField()),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formularios.formulario')),
            ],
        ),
    ]
