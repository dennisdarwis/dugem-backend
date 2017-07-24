import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import VenueList
from api.serializers import VenueListSerializer


@csrf_exempt
def venue_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        venues = VenueList.objects.all()
        serializer = VenueListSerializer(venues, many=True)
        data = {'responseCode': 0,
                'resposeDesc': 'Success',
                'venues': serializer.data}
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print("JSON BODY: "+str(data))
        serializer = VenueListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {'responseCode':0,
                    'resposeDesc':'Success'}
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
                'resposeDesc':'Success',
                'venues':serializer.data}
        return JsonResponse(data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VenueListSerializer(venue, data=data)
        if serializer.is_valid():
            serializer.save()
            data = {'responseCode': 0,
                    'resposeDesc': 'Success'}
            return JsonResponse(data, safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        venue.delete()
        data = {'responseCode': 0,
                'resposeDesc': 'Success'}
        return JsonResponse(data, safe=False)