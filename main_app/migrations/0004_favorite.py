# Generated by Django 4.1 on 2022-09-06 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_remove_profile_id_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.TextField()),
                ('name', models.TextField()),
                ('gender', models.TextField()),
                ('age', models.TextField()),
                ('breed', models.TextField()),
                ('size', models.TextField()),
                ('sterile', models.TextField()),
                ('shots', models.TextField()),
                ('description', models.TextField()),
                ('tags', models.TextField()),
                ('photos', models.TextField()),
                ('env_dogs', models.TextField()),
                ('env_cats', models.TextField()),
                ('env_child', models.TextField()),
                ('org_name', models.TextField()),
                ('org_mission', models.TextField()),
                ('org_city', models.TextField()),
                ('org_state', models.TextField()),
                ('org_email', models.TextField()),
                ('org_phone', models.TextField()),
                ('org_url', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]