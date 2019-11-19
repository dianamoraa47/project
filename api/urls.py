from django.urls import path, include
from .views import StudentViewSet
from rest_framework import routers

from .views import TeacherViewSet
from .views import CourseViewSet



router = routers.DefaultRouter()
router.register("students",StudentViewSet)
router.register("course",CourseViewSet)
router.register("teacher",TeacherViewSet)


urlpatterns =[
path("",include(router.urls)),
path("",include(router.urls)),
path("",include(router.urls)),

]
