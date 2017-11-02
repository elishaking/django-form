from django import forms
from .models import Member


# from crispy_forms.helper import FormHelper, Layout


class MembersForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter SURNAME first'}))
    name_of_next_of_kin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter SURNAME firsts'}),
                                          required=False)
    skills = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'eg. Singing, Dancing, Football, volleyball, Computerist, ...'}),
        required=False)

    # other_health_work = forms.CharField(widget=forms.TextInput(attrs={'class': 'hide'}), required=False)
    # other_other_work = forms.CharField(widget=forms.TextInput(attrs={'class': 'hide'}), required=False)

    class Meta:
        model = Member
        fields = ['full_name', 'gender', 'marital_status', 'phone', 'town', 'lga', 'state', 'email', 'residence',
                  'name_of_next_of_kin', 'address_of_next_of_kin', 'relation_with_next_of_kin',
                  'occupation', 'business_address', 'skills', 'sports',
                  'are_you_a_baptized_catholic', 'not_baptized', 'are_you_a_communicant', 'not_communicant',
                  'are_you_confirmed', 'not_confirmed', 'are_wedded_in_the_church', 'not_wedded',
                  'any_tribal_community', 'not_in_tribal_community', 'in_tribal_community',
                  'member_of_any_pius_society', 'not_in_pius_society', 'yes_In_pius_society',
                  'belongs_to_any_organ_in_church', 'dont_belong_to', 'yes_belong_to',
                  'catechetical_work', 'liturgical_work', 'security_work', 'environmental_work', 'health_work',
                  'other_health_work', 'sports', 'other_work', 'other_other_work']

        # def __init__(self, *args, **kwargs):
        #     super(BioDataForm, self).__init__(*args, **kwargs)
        #
        #     self.helper = FormHelper()
        #     self.helper.form_class = 'form-inline'
        #     self.helper.label_class = 'col-xs-6'
        #     self.helper.field_class = 'col-xs-6'
        #     self.helper.layout = Layout(
        #         'full_name',
        #         'gender',
        #     )


""""""
