from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from django_cutter.users.api.views import UserViewSet
from django_cutter.fitness.views import SetViewSet, ExerciseViewSet, WorkoutViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("sets", SetViewSet)
router.register("exercises", ExerciseViewSet)
router.register("workouts", WorkoutViewSet)


app_name = "api"
urlpatterns = router.urls
