from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cycle.models import Woman_Cycle
from cycle.serializers import WomenCycleSerializer
from cycle.utils import calculate_total_circles, create_event, validate_cycle_dates, validate_event_date

@csrf_exempt
@api_view(['POST'])
def create_cycle(request):
    """
    Create a cycle.
    """
    data = JSONParser().parse(request)
    is_dataset_ok = validate_cycle_dates(data)
    if not is_dataset_ok['status']:
      return Response({"error": is_dataset_ok['message']}, status=400)

    serializer = WomenCycleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        cycle = Woman_Cycle.objects.latest('id')
        total_created_cycles = calculate_total_circles(cycle)
        return Response({"total_created_cycles": total_created_cycles}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def cycle_event(request):
    """
    Get event on a lady’s cycle to happen on a day.
    """
    events = []
    date_string = request.GET.get('date')
    event_date = validate_event_date(date_string)
    if not event_date['status']:
      return Response({"error": event_date['message'], "date": date_string}, status=400)

    try:
        cycle = Woman_Cycle.objects.latest('id')
        events = create_event(event_date['data'], cycle)
    except Woman_Cycle.DoesNotExist:
        pass

    return Response(events, status=200)
