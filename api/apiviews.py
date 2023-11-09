"""
Views for an API
"""

from rest_framework import viewsets, response, decorators
from rest_framework.response import Response
from rest_framework.decorators import action
from api import models, serializer

# class UserViewSet(viewsets.ViewSet):
#     """"""

#     @action(detail=False)
#     def auth(self, request):
#         token = "as"
#         return Response({"token": token})

#     @action(detail=False)
#     def create(self, request):
#         return Response({})


class OwnerViewSet(viewsets.ModelViewSet):
    """Owner viewset"""

    queryset = models.Owner.objects.all()
    serializer_class = serializer.OwnerModelSerializer

    @decorators.action(detail=False, methods=["get"])
    def test(self, request):
        return response.Response({"message": "hello world"})


class SepciesViewSet(viewsets.ModelViewSet):
    """Species viewset"""

    queryset = models.Species.objects.all()
    serializer_class = serializer.SpeciesModelSerializer


class PetViewSet(viewsets.ModelViewSet):
    """Pet viewset"""

    queryset = models.Pet.objects.all()
    serializer_class = serializer.PetsModelSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """Record viewset"""

    queryset = models.Pet.objects.all()
    serializer_class = serializer.PetsModelSerializer
