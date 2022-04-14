# Generated by Django 4.0.2 on 2022-04-14 09:14

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField(default=0)),
                ('is_outside', models.BooleanField(default=False)),
                ('is_late', models.BooleanField(default=False)),
                ('rollno', models.IntegerField(default=0)),
                ('hostel', models.CharField(choices=[('Hostel A', 'Hostel A'), ('Hostel B', 'Hostel B'), ('Hostel C', 'Hostel C'), ('Hostel D', 'Hostel D'), ('Hostel E', 'Hostel E'), ('Hostel F', 'Hostel F'), ('Hostel G', 'Hostel G'), ('Hostel H', 'Hostel H'), ('Hostel I', 'Hostel I'), ('Hostel J', 'Hostel J'), ('Hostel K', 'Hostel K'), ('Hostel L', 'Hostel L'), ('Hostel M', 'Hostel M'), ('Hostel N', 'Hostel N'), ('Hostel O', 'Hostel O')], max_length=200)),
                ('video', models.FileField(upload_to=users.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('entry', 'Entry'), ('exit', 'Exit')], max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('hostel', models.CharField(choices=[('Hostel A', 'Hostel A'), ('Hostel B', 'Hostel B'), ('Hostel C', 'Hostel C'), ('Hostel D', 'Hostel D'), ('Hostel E', 'Hostel E'), ('Hostel F', 'Hostel F'), ('Hostel G', 'Hostel G'), ('Hostel H', 'Hostel H'), ('Hostel I', 'Hostel I'), ('Hostel J', 'Hostel J'), ('Hostel K', 'Hostel K'), ('Hostel L', 'Hostel L'), ('Hostel M', 'Hostel M'), ('Hostel N', 'Hostel N'), ('Hostel O', 'Hostel O')], max_length=200)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
