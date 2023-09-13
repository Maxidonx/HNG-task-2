from peopleAPI.views import InternsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Interns',InternsViewset)