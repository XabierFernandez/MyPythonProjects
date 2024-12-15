from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Guest

# Temporary storage for guest names
guest_list = []


def homepage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Guest.objects.create(name=name)  # Add the name to the database
        return HttpResponseRedirect("/")

    # Fetch all guest names from the database
    guests = Guest.objects.all()
    return render(request, "myapp/homepage.html", {"guests": guests})

def delete_guest(request, guest_id):
    guest = get_object_or_404(Guest, id=guest_id)
    guest.delete()
    return HttpResponseRedirect("/")
