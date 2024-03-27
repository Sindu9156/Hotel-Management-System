from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def hotel(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template=loader.get_template('About.html')
    return HttpResponse(template.render())
def roominfo(request):
    template=loader.get_template('Room.html')
    return HttpResponse(template.render())
def booking(request):
    template=loader.get_template('booking.html')
    return HttpResponse(template.render())
def contact(request):
    template=loader.get_template('Contact.html')
    return HttpResponse(template.render())