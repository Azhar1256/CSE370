# Generated by Django 3.1.7 on 2021-09-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covapp', '0002_auto_20210903_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccineregistration',
            name='a_vac',
            field=models.CharField(choices=[('MODERNA', 'MODERNA'), ('SINOPHARM', 'SINOPHARM'), ('PFIZER', 'PFIZER'), ('ASTRAZENECA', 'ASTRAZENECA'), ('Not Assigned', 'Not Assigned')], default='Not Assigned', max_length=50),
        ),
    ]
