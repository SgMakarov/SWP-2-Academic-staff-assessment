# Generated by Django 3.0.4 on 2020-04-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_survey_publish_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'text (multiple line)'), ('short-text', 'short text (one line)'), ('radio', 'radio'), ('select', 'select'), ('select-multiple', 'Select Multiple'), ('select_image', 'Select Image'), ('integer', 'integer'), ('float', 'float'), ('date', 'date')], default='text', max_length=200, verbose_name='Type'),
        ),
    ]
