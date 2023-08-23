from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from consultation.models import Consultant

from consultation.logic import consultation_create
from consultation.serializers import ConsultantSerializer, ConsultationSerializer


class ConsultantsAPIView(generics.ListAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    permission_classes = [IsAuthenticated]


class ConsultationsAPIView(generics.ListCreateAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return consultation_create(request)


class ConsultationDetailAPIView(generics.RetrieveAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
