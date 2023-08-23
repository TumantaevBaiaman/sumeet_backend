from django.urls import path
from consultation.views import (
    ConsultantsAPIView,
    ConsultationsAPIView,
    ConsultationDetailAPIView,
)


urlpatterns = [
    path("consultants/", ConsultantsAPIView.as_view(), name="consultants_list"),
    path("consultations/", ConsultationsAPIView.as_view(), name="consultations"),
    path(
        "consultations/<str:id>/",
        ConsultationDetailAPIView.as_view(),
        name="consultation_detail",
    ),
]
