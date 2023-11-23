
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'api/usuario', views.UsuarioViewSet, 'usuario')
router.register(r'api/objetivos', views.ObjetivoViewSet, 'objetivos')
router.register(r'api/empresas-objetivos', views.EmpresaObjetivosViewSet, 'empresas/objetivos')
router.register(r'api/compradores', views.CompradorViewSet, 'compradores')

urlpatterns = router.urls

