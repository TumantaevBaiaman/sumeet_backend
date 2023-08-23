import asyncio

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from consultation.models import Consultant, Question
from consultation.tasks import process_data


@transaction.atomic
def consultation_create(request):
    """
    create consultation
    """
    data = request.data
    consultant_id = data.get("consultant")
    try:
        consultant = Consultant.objects.get(id=consultant_id)
    except Consultant.DoesNotExist:
        return Response({"error": "Consultant not found"}, status=status.HTTP_400_BAD_REQUEST)

    new_question = Question.objects.create(
        user=request.user,
        consultant=consultant,
        topic=data.get("topic"),
        text=data.get("text"),
        result=data.get("result"),
    )

    response_data = {
        "message": "Consultation created successfully",
        "question_id": new_question.id,
    }

    process_data.delay(new_question.id)

    return Response(response_data, status=status.HTTP_201_CREATED)
