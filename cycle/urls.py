from django.urls import path
from cycle import views

urlpatterns = [
    path('create-cycles', views.create_cycle),
    path('cycle-event', views.cycle_event),
]