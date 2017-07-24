from rest_framework import serializers

from api.models import VenueList


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