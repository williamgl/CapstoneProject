# Generated by Django 4.1.2 on 2022-10-31 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.quiz')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
