from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import View
from rest_framework import generics
from .models import Tasks
from .serializers import TaskSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
        
def index(request):
    data_dict = {
        'data_insert': 'Test JSON data from DJANGO'
    }
    return render(request, 'test1/index.html', data_dict)


@api_view(['GET', 'POST', 'DELETE'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        queryset = Tasks.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == "DELETE":
        # print(request.data['id'])
        task = Tasks.objects.get(pk = request.data['id'])
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        print(request.data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
