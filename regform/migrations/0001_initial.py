# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=60, verbose_name='Full name:')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender:')),
                ('marital_status', models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Married'), ('W', 'Widow'), ('W', 'Widower'), ('Se', 'Separated')], max_length=2, verbose_name='Marital Status:')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='Phone:')),
                ('town', models.CharField(blank=True, max_length=100, verbose_name='Town:')),
                ('lga', models.CharField(blank=True, max_length=100, verbose_name='LGA:')),
                ('state', models.CharField(blank=True, max_length=100, verbose_name='State of Origin:')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='Email Address: (example: abc@example.com)')),
                ('residence', models.CharField(blank=True, max_length=300, verbose_name='Home Address:')),
                ('name_of_next_of_kin', models.CharField(blank=True, max_length=100, verbose_name='Name of next of Kin:')),
                ('address_of_next_of_kin', models.CharField(blank=True, max_length=200, verbose_name='Address of next kin:')),
                ('relation_with_next_of_kin', models.CharField(blank=True, max_length=100, verbose_name='Relationship with next of kin:')),
                ('occupation', models.CharField(blank=True, max_length=100, verbose_name='Occupation:')),
                ('business_address', models.CharField(blank=True, max_length=200, verbose_name='Business Address:')),
                ('skills', models.CharField(blank=True, max_length=100, verbose_name='Skills/Talents:')),
                ('are_you_a_baptized_catholic', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you a babtized catholic ?')),
                ('not_baptized', models.CharField(blank=True, max_length=300, verbose_name='If no, please, state your reasons:')),
                ('are_you_a_communicant', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you a communicant ? ')),
                ('not_communicant', models.CharField(blank=True, max_length=300, verbose_name='If no, please, state your reasons')),
                ('are_you_confirmed', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you confirmed ? ')),
                ('not_confirmed', models.CharField(blank=True, max_length=300, verbose_name='If no, please, state your reasons:')),
                ('are_wedded_in_the_church', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you wedded in the church ? ')),
                ('not_wedded', models.CharField(blank=True, max_length=300, verbose_name='If no, please, state your reasons:')),
                ('any_tribal_community', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Do you belong to any tribal communities in the church ? ')),
                ('not_in_tribal_community', models.CharField(blank=True, max_length=300, verbose_name='If no, please, state reasons:')),
                ('in_tribal_community', models.CharField(blank=True, max_length=300, verbose_name='If yes, please, state the community:')),
                ('member_of_any_pius_society', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Are you a member of any pius societies in the church ? ')),
                ('not_in_pius_society', models.CharField(blank=True, max_length=300, verbose_name='If no, please state your reasons:')),
                ('yes_In_pius_society', models.CharField(blank=True, max_length=300, verbose_name='If yes, please, state the society:')),
                ('belongs_to_any_organ_in_church', models.CharField(blank=True, choices=[('W', 'CWO'), ('M', 'CMO'), ('C', 'CYON')], max_length=1, verbose_name='Do you belong to any of the three organs in the church ?')),
                ('dont_belong_to', models.CharField(blank=True, max_length=300, verbose_name='If no, please state reasons:')),
                ('yes_belong_to', models.CharField(blank=True, max_length=300, verbose_name='If yes, please, state your role:')),
                ('catechetical_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Teaching Catechisms', 'Teaching Catechisms'), ('Teaching in sunday school', 'Teaching in sunday school'), ('Teaching in marriage course', 'Teaching in marriage course'), ('Infant Baptism class', 'Infant Baptism class')], max_length=100)),
                ('liturgical_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Choir', 'Choir'), ('Layreader', 'Proclamation(Layreader/Lector)'), ('Church warden', 'Church wardens'), ('Alter Service', 'Alter Service')], max_length=100)),
                ('security_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MOD', 'MOD'), ('Boys Brigade', 'Boys Brigade'), ('Security committee', 'Security committee'), ('I am a security personnel', 'I am a security personnel'), ('N/A', 'None')], max_length=100)),
                ('environmental_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Personal church cleaning', 'Personal church cleaning'), ('Gardenning', 'Gardenning'), ('Societal church cleaning', 'Societal church cleaning'), ('Done this in the past', 'I used to clean the church'), ('I clean the church', 'I do clean the church'), ('None', 'Not apply')], max_length=100)),
                ('health_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Health committee', 'Health committee'), ('Medical practitioner', 'Medical practitioner'), ('Midwifing', 'Midwifing'), ('Not my field', 'Not my occupation'), ('Other', 'Other, please specify')], max_length=100)),
                ('sports', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Sports committee', 'Sports committee'), ('Trainer/Coach', 'Trainer/Coach'), ('Umpire', 'Umpire'), ('Count me out', 'Count me out'), ('Sport team', 'Sport team')], max_length=100)),
                ('other_work', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Harvest and Bazaar', 'Harvest and Bazaar'), ('Fund raising', 'Fund raising'), ('Building/Project', 'Building/Project'), ('Enlightenment and Awareness', 'Enlightenment and Awareness'), ('Finance', 'Finance'), ('Other', 'Other, please specify')], max_length=100)),
            ],
        ),
    ]