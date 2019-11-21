# Generated by Django 2.2.7 on 2019-11-21 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('headcount_db', '0015_auto_20191121_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancetransaction',
            name='classroom',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='headcount_db.Classroom'),
        ),
        migrations.AlterField(
            model_name='attendancetransaction',
            name='student',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='headcount_db.Student'),
        ),
    ]