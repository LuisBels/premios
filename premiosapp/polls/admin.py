from django.contrib import admin
from .models import Question,Choice

class ChoiceAdmin(admin.StackedInline):
  model = Choice
  extra = 3


class QuestionAdmin(admin.ModelAdmin):
  inlines = [ChoiceAdmin]
  list_display = ("question_text", "pub_date")
  list_filter = ["pub_date"]
  search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)