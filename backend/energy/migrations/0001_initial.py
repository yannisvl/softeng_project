# Generated by Django 3.0.3 on 2020-03-02 11:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('is_staff', models.IntegerField(default=0)),
                ('is_active', models.IntegerField(default=1)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2020, 3, 2, 11, 18, 28, 758970))),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Actualtotalload',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('actiontaskid', models.BigIntegerField(db_column='ActionTaskID')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=2, null=True)),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.IntegerField(db_column='Month')),
                ('day', models.IntegerField(db_column='Day')),
                ('datetime', models.DateTimeField(db_column='DateTime')),
                ('areaname', models.CharField(blank=True, db_column='AreaName', max_length=200, null=True)),
                ('updatetime', models.DateTimeField(db_column='UpdateTime')),
                ('totalloadvalue', models.DecimalField(db_column='TotalLoadValue', decimal_places=2, max_digits=24)),
                ('rowhash', models.CharField(blank=True, db_column='RowHash', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ActualTotalLoad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aggregatedgenerationpertype',
            fields=[
                ('id', models.BigIntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('actiontaskid', models.BigIntegerField(db_column='ActionTaskID')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=2, null=True)),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.IntegerField(db_column='Month')),
                ('day', models.IntegerField(db_column='Day')),
                ('datetime', models.DateTimeField(db_column='DateTime')),
                ('areaname', models.CharField(blank=True, db_column='AreaName', max_length=200, null=True)),
                ('updatetime', models.DateTimeField(db_column='UpdateTime')),
                ('actualgenerationoutput', models.DecimalField(db_column='ActualGenerationOutput', decimal_places=2, max_digits=24)),
                ('actualconsuption', models.DecimalField(db_column='ActualConsuption', decimal_places=2, max_digits=24)),
                ('rowhash', models.CharField(blank=True, db_column='RowHash', max_length=255, null=True)),
            ],
            options={
                'db_table': 'AggregatedGenerationPerType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Allocatedeicdetail',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('mrid', models.CharField(blank=True, db_column='MRID', max_length=250, null=True)),
                ('docstatusvalue', models.CharField(blank=True, db_column='DocStatusValue', max_length=250, null=True)),
                ('attributeinstancecomponent', models.CharField(blank=True, db_column='AttributeInstanceComponent', max_length=250, null=True)),
                ('longnames', models.CharField(blank=True, db_column='LongNames', max_length=250, null=True)),
                ('displaynames', models.CharField(blank=True, db_column='DisplayNames', max_length=250, null=True)),
                ('lastrequestdateandortime', models.DateTimeField(blank=True, db_column='LastRequestDateAndOrTime', null=True)),
                ('deactivaterequestdateandortime', models.DateTimeField(blank=True, db_column='DeactivateRequestDateAndOrTime', null=True)),
                ('marketparticipantstreetaddresscountry', models.CharField(blank=True, db_column='MarketParticipantStreetAddressCountry', max_length=250, null=True)),
                ('marketparticipantacercode', models.CharField(blank=True, db_column='MarketParticipantACERCode', max_length=250, null=True)),
                ('marketparticipantvatcode', models.CharField(blank=True, db_column='MarketParticipantVATcode', max_length=250, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('eicparentmarketdocumentmrid', models.CharField(blank=True, db_column='EICParentMarketDocumentMRID', max_length=250, null=True)),
                ('elcresponsiblemarketparticipantmrid', models.CharField(blank=True, db_column='ELCResponsibleMarketParticipantMRID', max_length=250, null=True)),
                ('isdeleted', models.TextField(db_column='IsDeleted')),
            ],
            options={
                'db_table': 'AllocatedEICDetail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Areatypecode',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('areatypecodetext', models.CharField(blank=True, db_column='AreaTypeCodeText', max_length=255, null=True, unique=True)),
                ('areatypecodenote', models.CharField(blank=True, db_column='AreaTypeCodeNote', max_length=255, null=True)),
            ],
            options={
                'db_table': 'AreaTypeCode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dayaheadtotalloadforecast',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('actiontaskid', models.BigIntegerField(db_column='ActionTaskID')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=2, null=True)),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.IntegerField(db_column='Month')),
                ('day', models.IntegerField(db_column='Day')),
                ('datetime', models.DateTimeField(db_column='DateTime')),
                ('areaname', models.CharField(blank=True, db_column='AreaName', max_length=200, null=True)),
                ('updatetime', models.DateTimeField(db_column='UpdateTime')),
                ('totalloadvalue', models.DecimalField(db_column='TotalLoadValue', decimal_places=2, max_digits=24)),
                ('rowhash', models.CharField(blank=True, db_column='RowHash', max_length=255, null=True)),
            ],
            options={
                'db_table': 'DayAheadTotalLoadForecast',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mapcode',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('mapcodetext', models.CharField(blank=True, db_column='MapCodeText', max_length=255, null=True, unique=True)),
                ('mapcodenote', models.CharField(blank=True, db_column='MapCodeNote', max_length=255, null=True)),
            ],
            options={
                'db_table': 'MapCode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productiontype',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('productiontypetext', models.CharField(blank=True, db_column='ProductionTypeText', max_length=255, null=True, unique=True)),
                ('productiontypenote', models.CharField(blank=True, db_column='ProductionTypeNote', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ProductionType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resolutioncode',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('resolutioncodetext', models.CharField(blank=True, db_column='ResolutionCodeText', max_length=255, null=True, unique=True)),
                ('resolutioncodenote', models.CharField(blank=True, db_column='ResolutionCodeNote', max_length=255, null=True)),
            ],
            options={
                'db_table': 'ResolutionCode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.IntegerField()),
                ('remainingquota', models.IntegerField(default=100)),
                ('last_activity', models.DateTimeField(default=datetime.datetime(2017, 12, 30, 12, 0))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
