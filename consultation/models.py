import uuid

from django.db import models

from users.models import User


class Consultant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telegram_id = models.BigIntegerField("ID телеграм", unique=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "консультант"
        verbose_name_plural = "консультанты"

    def __str__(self) -> str:
        return f"Consultant ID: {self.id}"


class Question(models.Model):
    topic_choices = (
        (1, "Topic 1"),
        (2, "Topic 2"),
        (3, "Topic 3"),
        (4, "Topic 4"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    topic = models.IntegerField(choices=topic_choices)
    text = models.TextField()
    result = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    def __str__(self):
        return f"Question ID: {self.id}"


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"

    def __str__(self):
        return f"Answer ID: {self.id}"
