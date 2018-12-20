from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'collectionpoints', views.CollectionPointViewSet)
router.register(r'healthinsurances', views.HealthInsuranceViewSet)
router.register(r'exams', views.ExamViewSet)
router.register(r'serviceordercreate', views.ServiceOrderCreationViewSet, base_name='serviceordercreate')
router.register(r'serviceorderexam', views.ServiceOrderExamViewSet)

app_name = 'serviceOrder'

urlpatterns = [
    url(r'^', include(router.urls)),
    url('serviceorders', views.ServiceOrderByCollectionPoint.as_view())
]