from apps.reservation.models import Reservation
from django.contrib import admin


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
