from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404 

# Create your views here.
def chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,"ai1/chai.html",{'chais':chais})

def details(request,chai_id):
    chai = ChaiVarity.objects.get(id=chai_id)
    return render(request,"ai1/details.html",{'chai':chai})
