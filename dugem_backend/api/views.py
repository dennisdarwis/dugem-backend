import json

from django.db.models import Q
from django.db.models.functions import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import VenueList, EventList
from api.serializers import VenueListSerializer, EventListSerializer


@csrf_exempt
def venue_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        venues = VenueList.objects.all()
        serializer = VenueListSerializer(venues, many=True)
        data = {'responseCode': 0,
                'responseDesc': 'Success',
                'venues': serializer.data}
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print("JSON BODY: "+str(data))
        serializer = VenueListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {'responseCode':0,
                    'responseDesc':'Success'}
            return JsonResponse(data, safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def venue_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        venue = VenueList.objects.get(pk=pk)
    except VenueList.DoesNotExist:
        return HttpResponse(json.dumps({'responseCode':404}),status=404)

    if request.method == 'GET':
        serializer = VenueListSerializer(venue)
        data = {'responseCode':0,
                'responseDesc':'Success',
                'venues':serializer.data}
        return JsonResponse(data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VenueListSerializer(venue, data=data)
        if serializer.is_valid():
            serializer.save()
            data = {'responseCode': 0,
                    'responseDesc': 'Success'}
            return JsonResponse(data, safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        venue.delete()
        data = {'responseCode': 0,
                'responseDesc': 'Success'}
        return JsonResponse(data, safe=False)

@csrf_exempt
def event_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        today = datetime.datetime.today()
        events = EventList.objects.filter(Q(event_date_time__gte=today)).order_by("event_date_time")
        serializer = EventListSerializer(events, many=True)
        event_and_venues = []
        for i in serializer.data:
            loDict = dict(i)
            venue_id = loDict['venue_id']
            print("loDict: "+str(loDict))
            venue = VenueList.objects.get(pk=venue_id)
            loSerializer = VenueListSerializer(venue).data
            loDict['venue_contact']=loSerializer['venue_contact']
            loDict['venue_address']=loSerializer['venue_address']
            loDict['venue_url']=loSerializer['venue_url']
            loDict['venue_city']=loSerializer['venue_city']
            loDict['venue_details']=loSerializer['venue_details']
            loDict['venue_lat_long']=loSerializer['venue_lat_long']
            loDict['venue_name']=loSerializer['venue_name']
            print("loSerializer: "+str(loSerializer))
            event_and_venues.append(loDict)
            #print(loSerializer.data)


        print(event_and_venues)

        data = {'responseCode': 0,
                'responseDesc': 'Success',
                'events': event_and_venues}
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print("JSON BODY: "+str(data))
        serializer = EventListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {'responseCode':0,
                    'responseDesc':'Success'}
            return JsonResponse(data, safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def event_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        event = EventList.objects.get(pk=pk)
    except EventList.DoesNotExist:
        return HttpResponse(json.dumps({'responseCode':404}),status=404)

    if request.method == 'GET':
        serializer = EventListSerializer(event)
        data = {'responseCode':0,
                'responseDesc':'Success',
                'events':serializer.data}
        return JsonResponse(data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        print(data)
        serializer = EventListSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            data = {'responseCode': 0,
                    'responseDesc': 'Success'}
            return JsonResponse(data, safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        data = {'responseCode': 0,
                'responseDesc': 'Success'}
        return JsonResponse(data, safe=False)