from datetime import datetime
from django.test import TestCase
from rest_framework.test import APIClient
from cycle.utils import calculate_total_circles, create_event

class WomanCycleApiTest(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.create_cycle_payload_1 = {
          "last_period_date": "2020-06-20",
          "cycle_average": 25,
          "period_average": 5,
          "start_date": "2020-07-25",
          "end_date": "2020-08-25"
      }
    self.create_event_pre_ovulation_window_1 = "2020-09-10"
    self.create_event_fertility_window_1 = "2020-09-11"
    self.create_event_post_ovulation_window_1 = "2020-09-20"

  def test_create_circle_case_1(self):
      date_format = "%Y-%m-%d"
      response = self.client.post("/womens-health/api/create-cycles", 
                                  self.create_cycle_payload_1, 
                                  format="json")
      self.assertEqual(response.status_code, 201)
      self.assertEqual(response.data, {'total_created_cycles': 1})

      response = self.client.get("/womens-health/api/cycle-event", 
                                  {'date': self.create_event_pre_ovulation_window_1}
                                )
      self.assertEqual(response.status_code, 200)
      self.assertEqual(
            response.data, 
            [{'event': 'pre_ovulation_window', 'date': datetime.strptime(self.create_event_pre_ovulation_window_1, date_format).date()}]
          )

      response = self.client.get("/womens-health/api/cycle-event", 
                                  {'date': self.create_event_fertility_window_1}
                                )
      self.assertEqual(response.status_code, 200)
      self.assertEqual(
            response.data, 
            [{'event': 'fertility_window', 'date': datetime.strptime(self.create_event_fertility_window_1, date_format).date()}]
          )

      response = self.client.get("/womens-health/api/cycle-event", 
                                  {'date': self.create_event_post_ovulation_window_1}
                                )
      self.assertEqual(response.status_code, 200)
      self.assertEqual(
            response.data, 
            [{'event': 'post_ovulation_window', 'date': datetime.strptime(self.create_event_post_ovulation_window_1, date_format).date()}]
          )