from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .models import Book
# Create your views here.

def index(request):
    return HttpResponse('testMywork')


def all(request):
    allCars=""
    allEntries=Car.objects.all()

    for eachElement in allEntries:
        allCars+= eachElement.Car
    return HttpResponse(allCars)



def greaterThan2010(request):
    onlyObjectsGreaterThan2010 = Car.objects.filter(years__gt = 2010)
    return HttpResponse(onlyObjectsGreaterThan2010)


#Funtions for Books

def allObjects(request):
    allBooks=''
    allBookEntries=Book.object.all()

    for eacjElement in allBookEntries:
        allBooks+= eacjElement.Book
        return HttpResponse(allBooks)
#
# def newBook(request):
#

