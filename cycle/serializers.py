from rest_framework import serializers
from cycle.models import Woman_Cycle

class WomenCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman_Cycle
        fields = ['id', 'last_period_date', 'cycle_average', 'period_average', 'start_date', 'end_date']