from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

app_name = 'centroidiomas'

urlpatterns = [
    # Aspirantes
    path('aspirante/', AspiranteView.as_view(), name='aspirante_view'),
    path('aspirantecreate/', AspiranteCreateView.as_view(), name='aspirante_create'),
    path('aspiranteupdate/<int:pk>', AspiranteUpdateView.as_view(), name='aspirante_update'),
    path('aspirantedelete/<int:pk>', AspiranteDeleteView.as_view(), name='aspirante_delete'),
    # Convocatoria inscripcion
    path('convocatoriainscripcion/', ConvocatoriaInsView.as_view(), name='convocatoriainscripcion_view'),
    path('convocatoriainscripcioncreate/', ConvocatoriaInsCreateView.as_view(), name='convocatoriainscripcion_create'),
    path('convocatoriainscripcionupdate/<int:pk>', ConvocatoriaInsUpdateView.as_view(), name='convocatoriainscripcion_update'),
    path('convocatoriainscripciondelete/<int:pk>', ConvocatoriaInsDeleteView.as_view(), name='convocatoriainscripcion_delete'),
    # Grupos
    path('grupos/', GruposView.as_view(), name='grupos_view'),
    path('gruposcreate/', GruposCreateView.as_view(), name='grupos_create'),
    path('gruposupdate/<int:pk>', GruposUpdateView.as_view(), name='grupos_update'),
    path('gruposdelete/<int:pk>', GruposDeleteView.as_view(), name='grupos_delete'),
    # Horarios
    path('horarios/', HorariosView.as_view(), name='horarios_view'),
    path('horarioscreate/', HorariosCreateView.as_view(), name='horarios_create'),
    path('horariosupdate/<int:pk>', HorariosUpdateView.as_view(), name='horarios_update'),
    path('horariosdelete/<int:pk>', HorariosDeleteView.as_view(), name='horarios_delete'),
    # Idiomas
    path('idioma/', IdiomaView.as_view(), name='idioma_view'),
    path('idiomacreate/', IdiomaCreateView.as_view(), name='idioma_create'),
    path('idiomaupdate/<int:pk>', IdiomaUpdateView.as_view(), name='idioma_update'),
    path('idiomadelete/<int:pk>', IdiomaDeleteView.as_view(), name='idioma_delete'),
    # inscripcion
    path('inscripcion/', InscripcionView.as_view(), name='inscripcion_view'),
    path('inscripcioncreate/', InscripcionCreateView.as_view(), name='inscripcion_create'),
    path('inscripcionupdate/<int:pk>', InscripcionUpdateView.as_view(), name='inscripcion_update'),
    path('inscripciondelete/<int:pk>', InscripcionDeleteView.as_view(), name='inscripcion_delete'),
    # Niveles
    path('niveles/', NivelesView.as_view(), name='niveles_view'),
    path('nivelescreate/', NivelesCreateView.as_view(), name='niveles_create'),
    path('nivelesupdate/<int:pk>', NivelesUpdateView.as_view(), name='niveles_update'),
    path('nivelesdelete/<int:pk>', NivelesDeleteView.as_view(), name='niveles_delete'),
    # Periodo Academico
    path('periodoacademico/', PeriodoAcademicoView.as_view(), name='periodoacademico_view'),
    path('periodoacademicocreate/', PeriodoAcademicoCreateView.as_view(), name='periodoacademico_create'),
    path('periodoacademicoupdate/<int:pk>', PeriodoAcademicoUpdateView.as_view(), name='periodoacademico_update'),
    path('periodoacademicodelete/<int:pk>', PeriodoAcademicoDeleteView.as_view(), name='periodoacademico_delete'),
    # Salon
    path('salon/', SalonView.as_view(), name='salon_view'),
    path('saloncreate/', SalonCreateView.as_view(), name='salon_create'),
    path('salonupdate/<int:pk>', SalonUpdateView.as_view(), name='salon_update'),
    path('salondelete/<int:pk>', SalonDeleteView.as_view(), name='salon_delete'),
    # Vistas aspirante
    path('createaspirante/', CreateAspiranteView.as_view(), name='create_aspirante'),
    path('aspiranteconvocatoriainscripcion/', ConvocatoriaAspiranteInsView.as_view(), name='aspiranteconvocatoriainscripcion_view'),
    path('inscripcionaspirante/', InscripcionAspiranteCreate, name='inscripcionaspirante_view'),
]
