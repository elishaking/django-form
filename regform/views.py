from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MembersForm


# Create your views here.
def register_member(request):
    def generate_id(pk):
        return 100500 + pk

    form = MembersForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            member = form.save()
            member.member_id = generate_id(member.pk)
            member.save()

            return registered(request, member)

    return render(request, 'reg_form.html', {'form': form})


def registered(request, member):
    return render(request, 'registered.html', {'member': member})
