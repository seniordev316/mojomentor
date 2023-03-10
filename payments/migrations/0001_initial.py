# Generated by Django 4.1.2 on 2023-02-02 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_session_id', models.CharField(max_length=255, null=True)),
                ('pay_status', models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Paid'), (2, 'Expired')])),
                ('amount', models.FloatField()),
                ('payer_email', models.CharField(max_length=255, null=True)),
                ('payer_name', models.CharField(max_length=255, null=True)),
                ('product_type', models.CharField(max_length=20, null=True)),
                ('product_id', models.PositiveBigIntegerField(null=True)),
                ('code', models.CharField(max_length=255, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='CoursePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.course')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'course_payments',
            },
        ),
    ]
