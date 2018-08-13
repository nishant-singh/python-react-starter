from rest_framework import serializers
from . models import question, user

class questionSerializer(serializers.ModelSerializer):
	class Meta:
		model=question
		fields=('ques_id','statement','op1','op2','op3','op4')

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=('user_id','username','quest')