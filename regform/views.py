from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MembersForm
from .models import Member
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div

# Div.template = 'section_1.html'

# Layout(
#     Div(
#         'full_name',
#         'gender', 
#         'marital_status', 
#         'phone', 'town', 
#         'lga', 'state', 'email', 'residence',
#                   'name_of_next_of_kin', 'address_of_next_of_kin', 'relation_with_next_of_kin',
#         template='section_1.html'
#     )
# )


# Create your views here.
def section_1(request):
    #global person
    form = MembersForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            bio_data = form.save()
            # person.bio_data = bio_data
            # person.save()
            return HttpResponseRedirect('section2')

    return render(request, 'section_1.html', {'form': form})


def section_2(request):
    form = MembersForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            specialization = form.save()
            # person.specialization = specialization
            # person.save()
            return HttpResponseRedirect('section3')

    return render(request, 'section_2.html', {'form': form})


def section_3(request):
    form = MembersForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            spiritual_data = form.save()
            # person.spiritual_data = spiritual_data
            # person.save()
            return HttpResponseRedirect('section4')

    return render(request, 'section_3.html', {'form': form})


def section_4(request):
    form = MembersForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            church_work_history = form.save()
            # person.church_work_history = church_work_history
            # person.save()
            print('form completed')
            return HttpResponseRedirect('registered')

    return render(request, 'section_4.html', {'form': form})


def registered(request):
    return render(request, 'registered.html')
