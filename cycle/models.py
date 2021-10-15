from django.db import models

class Woman_Cycle(models.Model):
    last_period_date = models.DateField(auto_now_add=False)
    cycle_average = models.PositiveIntegerField()
    period_average = models.PositiveIntegerField()
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return str(self.last_period_date)