# Generated by Django 3.2 on 2022-02-15 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_auto_20220206_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('original_bag', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders_unique', to='profiles.userprofile')),
            ],
        ),
    ]
