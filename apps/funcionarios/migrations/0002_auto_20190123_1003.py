# Generated by Django 2.0.7 on 2019-01-23 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresas', '0001_initial'),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='departamentos',
            field=models.ManyToManyField(to='departamentos.Departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
