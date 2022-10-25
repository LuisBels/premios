import datetime

from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionResultsTest(TestCase):
  def test_good_page(self):
    response = self.client.get("polls/results.html")
    self.assertEqual(response.status_code, 200)