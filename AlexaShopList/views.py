from django.shortcuts import render, redirect
from models import *
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def searches(request):
    searchEntries = Search.objects.all().order_by('-id')
    template = loader.get_template('searches.html')
    context = {
        'searchEntries': searchEntries,
    }
    return HttpResponse(template.render(context, request))


def offers(request, search_id):
    offerEntries = Offer.objects.filter(search_id__exact=int(search_id)).order_by('price')
    template = loader.get_template('offers.html')
    context = {
        'offerEntries': offerEntries,
    }
    return HttpResponse(template.render(context, request))


def choose(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    search = Search.objects.get(id=offer.search_id)
    search.chosen_offer = offer
    search.save()
    return offers(request, search.id)