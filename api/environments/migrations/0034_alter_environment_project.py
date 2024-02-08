# Generated by Django 3.2.23 on 2024-01-31 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_add_identity_overrides_migration_status'),
        ('environments', '0033_add_environment_feature_state_version_logic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='project',
            field=models.ForeignKey(help_text='Changing the project selected will remove all previous Feature States for the previously associated projects Features that are related to this Environment. New default Feature States will be created for the new selected projects Features for this Environment.', on_delete=django.db.models.deletion.DO_NOTHING, related_name='environments', to='projects.project'),
        ),
    ]