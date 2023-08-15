
from rest_framework import serializers

from Khoj_the_search_Page.models import InputData


class InputDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputData # catch InputData model from Khoj_the_search_Page
        fields = ["timestamp", "input_values"] # catch timestamp and input_values from Khoj_the_search_Page_inputdata Table
