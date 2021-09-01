# Generated by Django 3.2.6 on 2021-08-18 20:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetroUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('profile_pic', models.CharField(max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
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
        migrations.CreateModel(
            name='ColumnList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_deleted', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoginProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('name', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField()),
                ('is_deleted', models.BooleanField()),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('retro_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrouser_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('organization_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='organization', to='retro_api.organization')),
                ('retro_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrouser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RetroColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('sequence', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('vote', models.BooleanField()),
                ('comment', models.BooleanField()),
                ('reaction', models.BooleanField()),
                ('column_list_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='columnlist', to='retro_api.columnlist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Retrospective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('is_anonymous', models.BooleanField()),
                ('sprint_title', models.CharField(blank=True, max_length=255, null=True)),
                ('sprint_start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('sprint_end_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project', to='retro_api.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RetroStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('sequence', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RetroTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('sequence', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('like_count', models.IntegerField()),
                ('dislike_count', models.IntegerField()),
                ('retro_column_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrocolumn', to='retro_api.retrocolumn')),
                ('retrospective_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrospective_id', to='retro_api.retrospective')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RetroUserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('access_permission', models.JSONField()),
                ('description', models.CharField(max_length=200, null=True)),
                ('is_deleted', models.BooleanField()),
                ('role_type', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('is_deleted', models.BooleanField()),
                ('is_published', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('retro_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retro_user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemplateColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('sequence', models.IntegerField()),
                ('vote', models.BooleanField()),
                ('comment', models.BooleanField()),
                ('reaction', models.BooleanField()),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('column_list_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='column_list', to='retro_api.columnlist')),
                ('template_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='template', to='retro_api.template')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RetroTopicComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_anonymous', models.BooleanField()),
                ('retro_topic_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retro_topic', to='retro_api.retrotopic')),
                ('retro_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retro_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RetrospectiveCollaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('retro_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retro_user_idd', to=settings.AUTH_USER_MODEL)),
                ('retrospective_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrospectivee_id', to='retro_api.retrospective')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='retrospective',
            name='retro_stage_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrostage', to='retro_api.retrostage'),
        ),
        migrations.AddField(
            model_name='retrospective',
            name='retro_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retro_users_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retrospective',
            name='template_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='template_id', to='retro_api.template'),
        ),
        migrations.AddField(
            model_name='retrocolumn',
            name='retrospective_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrospectivee', to='retro_api.retrospective'),
        ),
        migrations.CreateModel(
            name='RetroAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('estimate_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('retro_topic_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrotopic', to='retro_api.retrotopic')),
                ('retro_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retro_users', to=settings.AUTH_USER_MODEL)),
                ('retrospective_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrospect_id', to='retro_api.retrospective')),
                ('status_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='status', to='retro_api.status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('retrospective_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrospective', to='retro_api.retrospective')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvitationRetroUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_created_ts', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Meta Created TimeStamp')),
                ('meta_updated_ts', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='Meta Updated TimeStamp')),
                ('invitation_code', models.CharField(max_length=255)),
                ('email', models.EmailField(default=True, max_length=255)),
                ('first_name', models.CharField(default=True, max_length=255)),
                ('invitation_status', models.CharField(choices=[('Notsent', 'Notsent'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled')], default='Notsent', max_length=255)),
                ('is_email_sent', models.BooleanField(default=False)),
                ('retro_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retros_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='retrouser',
            name='login_provider_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='loginprovider', to='retro_api.loginprovider'),
        ),
        migrations.AddField(
            model_name='retrouser',
            name='retro_user_role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retrouserrole', to='retro_api.retrouserrole'),
        ),
        migrations.AddField(
            model_name='retrouser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
