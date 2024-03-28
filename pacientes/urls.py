from rest_framework import routers
from .viewsets import PacienteViewset

router=routers.SimpleRouter()
router.register('pacientes', PacienteViewset)

urlpatterns = router.urls