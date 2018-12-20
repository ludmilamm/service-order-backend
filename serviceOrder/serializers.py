from rest_framework import serializers
from django.db.models import Q
from datetime import datetime
from dateutil.relativedelta import relativedelta
from serviceOrder.models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'description', 'state')

class NeighborhoodSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Neighborhood
        fields = ('id', 'description', 'city')

class PatientSerializer(serializers.ModelSerializer):
    neighborhood = NeighborhoodSerializer()

    class Meta:
        model = Patient
        fields = ('id', 'name', 'birthdate', 'gender', 'address', 'neighborhood')

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id', 'description')

class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'specialty')

class CollectionPointSerializer(serializers.ModelSerializer):
    neighborhood = NeighborhoodSerializer()

    class Meta: 
        model = CollectionPoint 
        fields = ('id', 'description', 'address', 'neighborhood')

class HealthInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInsurance
        fields = ('id', 'description')

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('id', 'description')

class ExamSerializer(serializers.ModelSerializer):
    sector = SectorSerializer()

    class Meta:
        model = Exam
        fields = ('id', 'description', 'biologicalMaterial', 'deadline', 'sector')

class HealthInsuranceExamPriceSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()
    helthInsurance = HealthInsuranceSerializer()

    class Meta:
        model = HealthInsuranceExamPrice
        fields = ('id', 'exam', 'healthInsurance', 'price')

class ServiceOrderExamSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)
    resultDate = serializers.CharField(read_only=True)
    price = serializers.CharField(read_only=True)

    class Meta:
        model = ServiceOrderExam
        fields = ('id', 'exam', 'resultDate', 'price', 'status')

class ServiceOrderSerializer(serializers.ModelSerializer):
    exams = ServiceOrderExamSerializer(many=True, read_only=True)
    patient = PatientSerializer()
    doctor = DoctorSerializer()
    healthInsurance = HealthInsuranceSerializer()
    collectionPoint = CollectionPointSerializer()

    class Meta:
        model = ServiceOrder
        fields = ('id', 'date', 'patient', 'healthInsurance', 'collectionPoint', 'doctor', 'exams')

class ServiceOrderCreationSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    healthInsurance = serializers.PrimaryKeyRelatedField(queryset=HealthInsurance.objects.all())
    collectionPoint = serializers.PrimaryKeyRelatedField(queryset=CollectionPoint.objects.all())
    exams = serializers.ListField(child=serializers.IntegerField())

    def create(self, validated_data):
        try:
            patient = Patient.objects.filter(id=validated_data.pop('patient')).first()
            healthInsurance = HealthInsurance.objects.filter(id=validated_data.pop('healthInsurance')).first()
            collectionPoint = CollectionPoint.objects.filter(id=validated_data.pop('collectionPoint')).first()
            doctor = Doctor.objects.filter(id=validated_data.pop('doctor')).first()
        except Exception as e:
            error = {'message': "Bad Request"}
            raise serializers.ValidationError(error)

        try:
            service_order = ServiceOrder.objects.create(patient=patient, healthInsurance=healthInsurance, collectionPoint=collectionPoint, doctor=doctor)
        except Exception as e:
            error = {'message': "Bad Request"}
            raise serializers.ValidationError(error)

        exam_ids = validated_data['exams']
        for exam_id in exam_ids:
            try:
                exam = Exam.objects.filter(id=exam_id).first()
            
                qHealthInsurance = Q(healthInsurance=healthInsurance)
                qExam = Q(exam=exam)

                healthInsuranceExamPrice = HealthInsuranceExamPrice.objects.filter(qHealthInsurance, qExam).first()
                price = healthInsuranceExamPrice.price

                resultDate = datetime.now() + relativedelta(days=exam.deadline)
            
                ServiceOrderExam.objects.create(serviceOrder=service_order, exam=exam, price=price, resultDate=resultDate)
            except Exception as e:
                error = {'message': "Bad Request"}
                service_order.delete()
                raise serializers.ValidationError(error)
        
        return ServiceOrderSerializer(service_order).data