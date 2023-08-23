from unittest.mock import patch, Mock

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from users.factories import UserFactory
from consultation.factories import ConsultantFactory
from consultation.views import (
    ConsultantsAPIView,
    ConsultationsAPIView,
    ConsultationDetailAPIView,
)


class ConsultantsViewTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = UserFactory()
        self.consultant = ConsultantFactory(user=self.user)

    def test_list_consultants(self):
        view = ConsultantsAPIView.as_view()
        request = self.factory.get(reverse("consultants_list"))
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_consultations_authenticated(self):
        view = ConsultationsAPIView.as_view()
        request = self.factory.get(reverse("consultations"))
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_consultations_unauthenticated(self):
        view = ConsultationsAPIView.as_view()
        request = self.factory.get(reverse("consultations"))
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_consultation_authenticated(self):
        view = ConsultationsAPIView.as_view()
        data = {
            "topic": 1,
            "consultant": str(self.consultant.id),
            "text": "test text",
            "result": "test result",
        }
        request = self.factory.post(reverse("consultations"), data=data)
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_consultation_unauthenticated(self):
        view = ConsultationsAPIView.as_view()
        data = {
            "topic": 1,
            "consultant": str(self.consultant.id),
            "text": "test text",
            "result": "test result",
        }
        request = self.factory.post(reverse("consultations"), data=data)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_consultation_authenticated(self):
        view = ConsultationDetailAPIView.as_view()
        request = self.factory.get(reverse("consultation_detail", args=[self.consultant.id]))
        force_authenticate(request, user=self.user)
        response = view(request, id=self.consultant.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_consultation_unauthenticated(self):
        view = ConsultationDetailAPIView.as_view()
        request = self.factory.get(reverse("consultation_detail", args=[self.consultant.id]))
        response = view(request, id=self.consultant.id)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
