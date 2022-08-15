# Generated by Django 2.2.16 on 2022-08-15 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220814_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_at', models.DateTimeField(auto_now_add=True, verbose_name='subscription date')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
                'ordering': ['-subscribed_at', 'id'],
            },
        ),
        migrations.AddConstraint(
            model_name='usersubscription',
            constraint=models.UniqueConstraint(fields=('subscriber', 'subscription'), name='unique_subscription'),
        ),
    ]
