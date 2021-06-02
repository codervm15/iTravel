from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def homepage(request):
    # dest1=Destination()
    # dest1.name="Mumbai"
    # dest1.img="destination_1.jpg"
    # dest1.desc="City that never sleeps"
    # dest1.price=500
    # dest1.offer=True
    #
    # dest2 = Destination()
    # dest2.name = "Bangelore"
    # dest2.img = "destination_2.jpg"
    # dest2.desc = "IT City"
    # dest2.price = 800
    # dest2.offer = False
    #
    # dest3 = Destination()
    # dest3.name = "Delhi"
    # dest3.img = "destination_3.jpg"
    # dest3.desc = "Capital of India"
    # dest3.price = 1000
    # dest3.offer = True

    dest=Destination.objects.all()
    context={'dest':dest}
    return render(request,'index.html',context)



