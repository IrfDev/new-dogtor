"""API Serializers"""

# They're like web forms, they're going to validate date before send them to the database

from rest_framework import serializers
from api import models


class OwnerModelSerializer(serializers.ModelSerializer):
    """Owner serializer"""

    class Meta:
        model = models.Owner
        fields = ("id", "first_name", "last_name", "phone", "email", "address")


class SpeciesModelSerializer(serializers.ModelSerializer):
    """Species serializer"""

    class Meta:
        model = models.Species
        fields = ("id", "name")


class PetsModelSerializer(serializers.ModelSerializer):
    """Pets serializer"""

    # owner = serializers.SlugRelatedField()

    class Meta:
        model = models.Pet
        fields = ("id", "name", "owner", "age", "species")
        read_only_fields = "created_at"


class RecordModelSerializer(serializers.ModelSerializer):
    """Record serializer"""

    class Meta:
        model = models.Record
        fields = ("category", "procedure", "pet", "date")
