from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import question, user
from . serializers import questionSerializer, userSerializer

class quesList(APIView):
    def get(request, user_id):

        userid = user.objects.all()
        #user_id=20
        usr = request.GET.get('user_id', '')
        q = get_object_or_404(userid, user_id=usr)

        object = question.objects.filter(ques_id=q.quest.ques_id)
        serializer = questionSerializer(object, many=True)
        return Response(serializer.data)
