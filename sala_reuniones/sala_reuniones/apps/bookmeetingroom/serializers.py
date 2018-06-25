from rest_framework import serializers
from .models import (
    BookMeetingRoom,
)


class BookMeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMeetingRoom
        fields = (
            'id',
            'date',
            'start_time',
            'end_time',
            'amount_of_people',
            'supplies',
            'meetingroom',
        )