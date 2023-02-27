from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id =serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    subject = serializers.CharField(max_length=25)