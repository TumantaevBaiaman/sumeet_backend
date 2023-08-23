from consultation.tasks import process_data
from django.test import TestCase, override_settings
from unittest.mock import patch

from users.factories import UserFactory
from rest_framework.test import APIRequestFactory
from consultation.factories import ConsultantFactory, QuestionFactory, AnswerFactory


class TestProcessData(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = UserFactory()
        self.consultant = ConsultantFactory()
        self.question = QuestionFactory()
        self.answer = AnswerFactory()

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @patch("consultation.tasks.send_message_async")
    def test_process_data(self, mocked_task):
        process_data(question_id=self.question.id)
        mocked_task.assert_called_once_with(question=self.question)
