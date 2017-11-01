from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


# Register your models here.

class MembersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'marital_status', 'residence', 'state', 'lga', 'email', 'gender', 'name_of_next_of_kin', 'address_of_next_of_kin', 'relation_with_next_of_kin',
                    'occupation', 'business_address', 'skills', 'sports', 
                    'are_you_a_baptized_catholic', 'not_baptized', 'are_you_a_communicant', 'not_communicant', 'are_you_confirmed',
                    'not_confirmed', 'are_wedded_in_the_church', 'not_wedded', 'any_tribal_community', 'not_in_tribal_community', 'in_tribal_community',
              		'member_of_any_pius_society', 'not_in_pius_society', 'yes_In_pius_society', 'belongs_to_any_organ_in_church', 
              		'dont_belong_to', 'yes_belong_to',
                    'catechetical_work', 'liturgical_work', 'security_work', 'environmental_work', 'health_work', 'sports', 'other_work')

    search_fields = ('full_name', 'state', 'lga', 'phone')

    fields = ['phone', 'marital_status', 'residence', 'state', 'lga', 'town', 'email', 'gender', 'name_of_next_of_kin', 'address_of_next_of_kin', 'relation_with_next_of_kin',
    		  'occupation', 'business_address', 'skills', 'sports', 'are_you_a_baptized_catholic', 'not_baptized', 'are_you_a_communicant', 'not_communicant', 'are_you_confirmed',
    		  'member_of_any_pius_society', 'not_in_pius_society', 'yes_In_pius_society', 'belongs_to_any_organ_in_church', 'dont_belong_to', 'yes_belong_to', 'catechetical_work', 'liturgical_work',
    		  'security_work', 'environmental_work', 'health_work', 'other_work',]


admin.site.register(Member, MembersAdmin)
admin.site.unregister(Group)



# 'are_you_a_baptized_catholic', 'not_baptized', 'are_you_a_communicant', 'not_communicant', 'are_you_confirmed',
#               'not_confirmed', 'are_wedded_in_the_church', 'not_wedded', 'any_tribal_community', 'not_in_tribal_community', 'in_tribal_community',
#               'member_of_any_pius_society', 'not_in_pius_society', 'yes_In_pius_society', 'belongs_to_any_organ_in_church', 
#               'dont_belong_to', 'yes_belong_to', 'catechetical_work', 'liturgical_work', 'security_work', 'environmental_work', 'health_work', 'sports', 'other_work',


