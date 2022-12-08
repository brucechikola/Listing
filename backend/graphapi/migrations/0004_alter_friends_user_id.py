# Generated by Django 4.1.3 on 2022-12-08 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('graphapi', '0003_rename_fid_friends_friend_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
