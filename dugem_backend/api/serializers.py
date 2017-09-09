from datetime import datetime

from rest_framework import serializers
from rest_framework.settings import api_settings

from api.models import VenueList, EventList


class VenueListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    venue_name = serializers.CharField(max_length=255, allow_blank=False)
    venue_url = serializers.CharField(max_length=255, allow_blank=False)
    venue_address = serializers.CharField(max_length=255, allow_blank=False)
    venue_lat_long = serializers.CharField(max_length=255, allow_blank=False)
    venue_contact = serializers.CharField(max_length=255, allow_blank=False)
    venue_details = serializers.CharField(max_length=255, allow_blank=False)
    venue_city = serializers.CharField(max_length=255, allow_blank=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return VenueList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.venue_name = validated_data.get('venue_name', instance.venue_name)
        instance.venue_url = validated_data.get('venue_url', instance.venue_url)
        instance.venue_address = validated_data.get('venue_address', instance.venue_address)
        instance.venue_lat_long = validated_data.get('venue_lat_long', instance.venue_lat_long)
        instance.venue_contact = validated_data.get('venue_contact', instance.venue_contact)
        instance.venue_details = validated_data.get('venue_details', instance.venue_details)
        instance.venue_city = validated_data.get('venue_city', instance.venue_city)
        instance.save()
        return instance


class EventListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    venue_id = serializers.IntegerField(allow_null=False)
    event_name = serializers.CharField(max_length=255, allow_blank=False)
    event_price = serializers.DecimalField(allow_null=False, max_digits=6, decimal_places=2)
    event_detail = serializers.CharField(max_length=255, allow_blank=False)
    #time_start_end = serializers.CharField(max_length=255, allow_blank=False)
    event_time_start = serializers.TimeField(format="%H:%M", input_formats=None)
    event_time_end = serializers.TimeField(format="%H:%M", input_formats=None)
    event_url = serializers.CharField(max_length=255, allow_blank=False)
    event_img_url = serializers.CharField(max_length=255, allow_blank=False)
    event_date_time = serializers.DateField(allow_null=False)

    def create(self, validated_data):
        return EventList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.venue_id = validated_data.get('venue_id', instance.venue_id)
        instance.event_name = validated_data.get('event_name', instance.event_name)
        instance.event_price = validated_data.get('event_price', instance.event_price)
        instance.event_detail = validated_data.get('event_detail', instance.event_detail)
        #instance.time_start_end = validated_data.get('time_start_end', instance.time_start_end)
        instance.event_time_start = validated_data.get('event_time_start', instance.event_time_start)
        instance.event_time_end = validated_data.get('event_time_end', instance.event_time_end)
        instance.event_url = validated_data.get('event_url', instance.event_url)
        instance.event_img_url = validated_data.get('event_img_url', instance.event_img_url)
        instance.event_date_time = validated_data.get('event_date_time', instance.event_date_time)
        instance.save()
        return instance