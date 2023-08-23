from django.test import TestCase
from consultation.models import Consultant, Question, Answer
from consultation.factories import ConsultantFactory, QuestionFactory, AnswerFactory
from django.db.utils import IntegrityError

from users.factories import UserFactory


class ModelTests(TestCase):
    def test_create_consultant(self):
        consultant = ConsultantFactory()
        self.assertIsInstance(consultant, Consultant)

    def test_create_question(self):
        question = QuestionFactory()
        self.assertIsInstance(question, Question)

    def test_create_answer(self):
        answer = AnswerFactory()
        self.assertIsInstance(answer, Answer)
