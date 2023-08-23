import factory
from consultation.models import Consultant, Question, Answer
from users.factories import UserFactory


class ConsultantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Consultant

    telegram_id = factory.Faker("pyint", min_value=100000, max_value=999999)
    user = factory.SubFactory(UserFactory)


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    topic = factory.Iterator([1, 2, 3, 4])
    user = factory.SubFactory(UserFactory)
    consultant = factory.SubFactory(ConsultantFactory)
    text = factory.Faker("paragraph")
    result = factory.Faker("paragraph")


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Answer

    question = factory.SubFactory(QuestionFactory)
    answer = factory.Faker("paragraph")
