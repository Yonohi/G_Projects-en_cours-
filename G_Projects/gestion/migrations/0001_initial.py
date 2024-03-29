# Generated by Django 4.0.5 on 2022-06-28 15:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grossiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_cours', models.BooleanField()),
                ('code_campagne', models.CharField(max_length=50)),
                ('code_kammi', models.CharField(max_length=50)),
                ('nb_jour_total', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('nb_jour_realise', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('prix', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date_debut', models.DateField(blank=True, null=True)),
                ('date_fin_prevue', models.DateField(blank=True, null=True)),
                ('date_fin_reelle', models.DateField(blank=True, null=True)),
                ('payeur', models.CharField(choices=[('F', 'Fournisseur'), ('G', 'Grossiste'), ('P', 'Partenaire')], max_length=50)),
                ('client_principal', models.CharField(choices=[('F', 'Fournisseur'), ('G', 'Grossiste'), ('P', 'Partenaire')], max_length=50)),
                ('has_objectif', models.BooleanField()),
                ('objectif', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('chef_projet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projets', to=settings.AUTH_USER_MODEL)),
                ('fournisseur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projets', to='gestion.fournisseur')),
                ('grossiste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projets', to='gestion.grossiste')),
                ('partenaire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projets', to='gestion.partenaire')),
            ],
        ),
        migrations.CreateModel(
            name='Teleacteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposition', models.DateField(blank=True, null=True)),
                ('commande', models.DateField(blank=True, null=True)),
                ('brief_demarrage', models.DateField(blank=True, null=True)),
                ('cr_brief', models.DateField(blank=True, null=True)),
                ('script', models.DateField(blank=True, null=True)),
                ('fichier', models.DateField(blank=True, null=True)),
                ('rep_int', models.DateField(blank=True, null=True)),
                ('rep_final', models.DateField(blank=True, null=True)),
                ('facture', models.DateField(blank=True, null=True)),
                ('reglement', models.DateField(blank=True, null=True)),
                ('commentaire', models.TextField(blank=True)),
                ('projet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion.project')),
            ],
            options={
                'verbose_name': 'To Do List',
                'verbose_name_plural': 'To Do Lists',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='teleacteurs',
            field=models.ManyToManyField(blank=True, related_name='projets', to='gestion.teleacteur'),
        ),
        migrations.CreateModel(
            name='Opportunite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead', models.IntegerField(default=0)),
                ('nursering', models.IntegerField(default=0)),
                ('fiche_info', models.IntegerField(default=0)),
                ('commentaire', models.TextField(blank=True)),
                ('projet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion.project')),
            ],
        ),
    ]
