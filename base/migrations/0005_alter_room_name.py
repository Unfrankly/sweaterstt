# Generated by Django 5.0.3 on 2024-03-08 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_topic_room_host_alter_room_name_message_room_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
