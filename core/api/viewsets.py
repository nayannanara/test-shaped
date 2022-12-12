from core.models import Patient, Exam
from core.api.serializers import PatientSerializer, ExamSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]


    def get_queryset(self):
        height = self.request.query_params.get('height', None)
        queryset = Exam.objects.all()

        if height:
            queryset = queryset.filter(height__gt=height)
        
            
        return queryset
