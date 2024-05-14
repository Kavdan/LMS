# Generated by Django 4.0.8 on 2024-05-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_alter_result_id_alter_takencourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='level',
            field=models.CharField(choices=[('Бакалавр', 'Степень бакалавра'), ('Магистр', 'Степень магистра')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='semester',
            field=models.CharField(choices=[('Первый', 'First'), ('Второй', 'Second')], max_length=100),
        ),
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[('СДАН', 'СДАН'), ('НЕ СДАН', 'НЕ СДАН')], max_length=200),
        ),
    ]
