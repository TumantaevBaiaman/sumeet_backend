from django.contrib import admin
from consultation.models import Consultant, Question, Answer


class AnsweredQuestionFilter(admin.SimpleListFilter):
    title = "Статус вопроса"
    parameter_name = "answered"

    def lookups(self, request, model_admin):
        return (
            ("answered", "Отвечен"),
            ("unanswered", "Неотвечен"),
        )

    def queryset(self, request, queryset):
        if self.value() == "answered":
            return queryset.filter(answer__isnull=False)
        elif self.value() == "unanswered":
            return queryset.filter(answer__isnull=True)


@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ("id", "telegram_id")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "consultant", "user")
    list_filter = (AnsweredQuestionFilter,)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "answer")
