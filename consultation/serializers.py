from rest_framework import serializers
from .models import Consultant, Answer, Question


class ConsultantSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")

    class Meta:
        model = Consultant
        fields = ["id", "telegram_id", "username", "first_name", "last_name"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "answer", "created"]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ["id", "topic", "text", "result", "created", "answer"]


class ConsultationSerializer(serializers.ModelSerializer):
    consultations = QuestionSerializer(many=True, source="question_set")
    username = serializers.ReadOnlyField(source="user.username")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    photo = serializers.ReadOnlyField(source="user.photo")

    class Meta:
        model = Consultant
        fields = ["id", "username", "first_name", "last_name", "photo", "consultations"]
