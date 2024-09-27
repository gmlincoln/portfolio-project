# Generated by Django 5.1.1 on 2024-09-27 02:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_Proficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SkillName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(choices=[('python', 'Python'), ('c++', 'C++'), ('java', 'Java'), ('javascript', 'Javascript'), ('php', 'Php')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('proficiency', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.skill_proficiency')),
                ('skill_name', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.skillname')),
            ],
        ),
    ]