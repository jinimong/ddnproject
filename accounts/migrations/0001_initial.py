# Generated by Django 2.1.3 on 2018-12-10 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def forward_func(apps, schema_editor):
    # 현재 모든 User에 대해서 Profile을 생성
    auth_user_model = settings.AUTH_USER_MODEL.split('.') # 'auth.User' 를 튜플로 분리
    User = apps.get_model(*auth_user_model)
    Profile = apps.get_model('accounts', 'Profile')

    for user in User.objects.all():
        print(f'Create profile User#{user.pk}')
        Profile.objects.create(user=user)


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('website_url', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(forward_func, reverse_func),
    ]
