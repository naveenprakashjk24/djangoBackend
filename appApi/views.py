from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import ProjectContractor,ProjectStagesMapping, ProjectStage, ProjectAssigningDetails
from .serializers import ProjectContractorSerializer, ProjectStageSerializer, ProjectstgMappingSerializer, ProjectAssignSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data="Only for loggin users", status=status.HTTP_200_OK)


# simple view without decorators
# @csrf_exempt
# def contractor_list(request):
#     if request.method == 'GET':
#          contractors = ProjectContractor.objects.all()
#          serializers = ProjectContractorSerializer(contractors, many=True)
#          return JsonResponse(serializers.data, safe=False)

#     elif request.method=='POST':
#         data = JSONParser().parse(request)
#         serializers = ProjectContractorSerializer(data=data)
#         if serializers.is_valid():
#              serializers.save()
#              return JsonResponse(serializers.data , status=status.HTTP_201_CREATED)

#         return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def contractor_details(request, pk):
#     try:
#         contractors= ProjectContractor.objects.get(id=pk)
#     except ProjectContractor.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#          serializers = ProjectContractorSerializer(contractors, many=False)
#          return JsonResponse(serializers.data, safe=False)

#     elif request.method == ('POST' or 'PUT'):
#         data = JSONParser().parse(request)
#         serializers = ProjectContractorSerializer(contractors, data=data)
#         if serializers.is_valid():
#              serializers.save()
#              return JsonResponse(serializers.data)

#         return JsonResponse(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         contractors.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# function based api view
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def contractor_list(request):
    # contractor list
    if request.method == 'GET':
        contractors = ProjectContractor.objects.all()
        serializers = ProjectContractorSerializer(contractors, many=True)
        return Response(serializers.data)

    # add contractor
    elif request.method == 'POST':
        serializers = ProjectContractorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def contractor_details(request, pk):
    try:
        contractors = ProjectContractor.objects.get(id=pk)
    except ProjectContractor.DoesNotExist:
        return Response({'Error': 'No data Found'}, status=status.HTTP_404_NOT_FOUND)

    # contractor details
    if request.method == 'GET':
        serializers = ProjectContractorSerializer(contractors, many=False)
        return Response(serializers.data)

    # update contactor
    elif request.method == ('POST' or 'PUT'):
        serializers = ProjectContractorSerializer(contractors, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete contactor
    elif request.method == 'DELETE':
        contractors.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# end function based view

# class based view

class StagesApiView(APIView):
    permission_classes = [IsAuthenticated]

    # stage lists
    def get(self, request):
        stages = ProjectStage.objects.all()
        serializers = ProjectStageSerializer(stages, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # add stages
    def post(self, request):
        serializers = ProjectStageSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class StageDetailsApiview(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return ProjectStage.objects.get(id=id)
        except ProjectStage.DoesNotExist:
            return HttpResponse({'Error': 'No data found'}, status=status.HTTP_404_NOT_FOUND)

    # stage details
    def get(self, request, id):
        stages = self.get_object(id)
        serializers = ProjectStageSerializer(stages)
        return Response(serializers.data, status=status.HTTP_200_OK)

    # update stage
    def post(self, request, id):
        stages = self.get_object(id)
        serializers = ProjectStageSerializer(stages, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete stage
    def delete(self, request, id):
        stages = self.get_object(id)
        stages.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# end class based view

# generic based view
# test


class ProjectstgMapping(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        mapping = ProjectStagesMapping.objects.all()
        serializers = ProjectstgMappingSerializer(mapping, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectstgMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectStgmapUpdate(APIView):
    permission_classes=[IsAuthenticated]
    def get_object(self, id):
        try:
            return ProjectStagesMapping.objects.get(id=id)
        except ProjectStagesMapping.DoesNotExist:
            return HttpResponse({'Error': 'No data found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        mapping =  self.get_object(id)
        serializer = ProjectstgMappingSerializer(mapping)
        return  Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        mapping = self.get_object(id)
        serializer = ProjectstgMappingSerializer(mapping, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        mapping = self.get_object(id)
        mapping.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class ProjectuserMapping(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        userMap = ProjectAssigningDetails.objects.all()
        serializer = ProjectAssignSerializer(userMap, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectAssignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProjectuserMappingupdate(APIView):
    permission_classes=[IsAuthenticated]

    def get_object(self, id):
        try:
            return ProjectAssigningDetails.objects.get(id=id)
        except ProjectAssigningDetails.DoesNotExist:
            return Response({'Error': 'No data found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        UsrMapping = self.get_object(id)
        serializer = ProjectAssignSerializer(UsrMapping)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, id):
        UserMapping = self.get_object(id)
        serializer = ProjectAssignSerializer(UserMapping, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        UsrMapping = self.get_object(id)
        UsrMapping.delete()
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
