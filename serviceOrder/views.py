from rest_framework import viewsets, generics
from rest_framework.response import Response
from serviceOrder.models import *
from serviceOrder.serializers import *

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class CollectionPointViewSet(viewsets.ModelViewSet):
    queryset = CollectionPoint.objects.all()
    serializer_class = CollectionPointSerializer

class HealthInsuranceViewSet(viewsets.ModelViewSet):
    queryset = HealthInsurance.objects.all()
    serializer_class = HealthInsuranceSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ServiceOrderExamViewSet(viewsets.ModelViewSet):
    queryset = ServiceOrderExam.objects.all()
    serializer_class = ServiceOrderExamSerializer

class ServiceOrderViewSet(viewsets.ModelViewSet):
    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer

class ServiceOrderCreationViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceOrderCreationSerializer

    def create(self, request):
        serializer = ServiceOrderCreationSerializer(request.data)
        return Response(serializer.create(request.data))

class ServiceOrderByCollectionPoint(generics.ListAPIView):
    serializer_class = ServiceOrderSerializer

    def get_queryset(self):
        queryset = ServiceOrder.objects.all()
        collectionPointId = self.request.query_params.get('collection_point', None)
        if (collectionPointId is not None):
            queryset = queryset.filter(collectionPoint=collectionPointId)
        patient = self.request.query_params.get('patient', None)
        if (patient is not None):
            queryset = queryset.filter(patient__name__icontains=patient)    
        return queryset
    