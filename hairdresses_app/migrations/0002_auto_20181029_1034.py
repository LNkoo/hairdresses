# Generated by Django 2.1.2 on 2018-10-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairdresses_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hairdo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва зачіски')),
                ('price', models.FloatField(verbose_name='Вартість')),
                ('sex', models.CharField(choices=[('MALE', 'Чоловіча'), ('FEMALE', 'Жіноча')], max_length=15, verbose_name='Стать')),
                ('washing', models.BooleanField(default=False, verbose_name='Миття волосся')),
                ('drying', models.BooleanField(default=False, verbose_name='Сушіння волосся')),
                ('fixing', models.BooleanField(default=False, verbose_name='Укладка волосся')),
            ],
            options={
                'verbose_name': 'зачіска',
                'verbose_name_plural': 'Зачіски',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=255, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='client',
            name='sign_regular_customer',
            field=models.BooleanField(default=False, verbose_name='Постійний клієнт'),
        ),
        migrations.AlterField(
            model_name='client',
            name='surname',
            field=models.CharField(max_length=255, verbose_name='Прізвище'),
        ),
    ]