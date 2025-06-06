# Generated by Django 5.1.7 on 2025-05-19 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_lesson_created_at_lesson_description_lesson_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='correct_option',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option_a',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option_b',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option_c',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='option_d',
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_answer',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='option_3',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='lesson',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='learning.lesson'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.TextField(),
        ),
    ]
