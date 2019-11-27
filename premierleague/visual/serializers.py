from rest_framework import serializers
from .models import File
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class Player(serializers.Serializer):
		full_name = serializers.CharField(max_length=100,required=False)
		age = serializers.IntegerField(default=0)
		league = serializers.CharField(max_length=100,required=False)
		position = serializers.CharField(max_length=100,required=False)
		current_Club = serializers.CharField(max_length=100,required=False)
		minutes_played_overall = serializers.IntegerField(default=0)
		nationality= serializers.CharField(max_length=100,required=False)
		appearances_overall = serializers.IntegerField(default=0)
		goals_overall = serializers.IntegerField(default=0)
		goals_home = serializers.IntegerField(default=0)
		goals_away = serializers.IntegerField(default=0)
		assists_overall = serializers.IntegerField(default=0)
		clean_sheets_overall = serializers.IntegerField(default=0)
		yellow_cards_overall = serializers.IntegerField(default=0)
		red_cards_overall = serializers.IntegerField(default=0)