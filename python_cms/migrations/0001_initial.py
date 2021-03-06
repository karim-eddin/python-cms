# Generated by Django 2.1.12 on 2019-09-23 19:06

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import djcms_custom_menu.models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='DJCMSCustomMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('pages', jsonfield.fields.JSONField(blank=True, default=[], null=True)),
                ('site', models.ForeignKey(default=djcms_custom_menu.models.get_current_site, help_text='The site the menu is accessible at.', on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'DJCMS Menu',
                'verbose_name_plural': 'DJCMS Menus',
            },
        ),
        migrations.AlterUniqueTogether(
            name='djcmscustommenu',
            unique_together={('slug', 'site')},
        ),
    ]
