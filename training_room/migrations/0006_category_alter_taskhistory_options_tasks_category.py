# Generated by Django 4.0.3 on 2022-04-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_room', '0005_alter_taskhistory_options_profile_last_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='taskhistory',
            options={'ordering': ['date_last', '-date_start', 'right_answers', '-wrong_answers'], 'verbose_name': 'история заданий пользователя', 'verbose_name_plural': 'истории заданий пользователей'},
        ),
        migrations.AddField(
            model_name='tasks',
            name='category',
            field=models.ManyToManyField(to='training_room.category', verbose_name='категории'),
        ),
    ]
