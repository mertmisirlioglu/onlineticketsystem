# Generated by Django 2.2.1 on 2019-12-23 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('quota', models.IntegerField()),
                ('price', models.IntegerField()),
                ('isAvailable', models.BooleanField(default=False)),
                ('isAccepted', models.BooleanField(default=False)),
                ('rules', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('quota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.Event')),
            ],
            bases=('website.event',),
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.Event')),
            ],
            bases=('website.event',),
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.Event')),
            ],
            bases=('website.event',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birthday', models.DateField()),
                ('phone_number', models.CharField(max_length=11)),
                ('img', models.URLField(blank=True, null=True)),
                ('isOperator', models.BooleanField(default=False)),
                ('balance', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Stage'),
        ),
    ]