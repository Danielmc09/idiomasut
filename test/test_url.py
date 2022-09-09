from django.test import SimpleTestCase
from django.urls import reverse, resolve

from app.centroidiomas.views import *

class TestUrls(SimpleTestCase):

    #Test url aspirante
    def test_list_url_aspirante(self):
        url = reverse('centroidiomas:aspirante_view')
        self.assertEquals(resolve(url).func.view_class, AspiranteView)

    def test_create_url_aspirante(self):
        url = reverse('centroidiomas:aspirante_create')
        self.assertEquals(resolve(url).func.view_class, AspiranteCreateView)

    def test_update_url_aspirante(self):
        url = reverse('centroidiomas:aspirante_update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, AspiranteUpdateView)

    def test_delete_url_aspirante(self):
        url = reverse('centroidiomas:aspirante_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, AspiranteDeleteView)

    #Test url grupos
    def test_list_url_grupos(self):
        url = reverse('centroidiomas:grupos_view')
        self.assertEquals(resolve(url).func.view_class, GruposView)

    def test_create_url_grupos(self):
        url = reverse('centroidiomas:grupos_create')
        self.assertEquals(resolve(url).func.view_class, GruposCreateView)

    def test_update_url_grupos(self):
        url = reverse('centroidiomas:grupos_update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, GruposUpdateView)

    def test_delete_url_grupos(self):
        url = reverse('centroidiomas:grupos_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, GruposDeleteView)

    #Test url horarios
    def test_list_url_horarios(self):
        url = reverse('centroidiomas:horarios_view')
        self.assertEquals(resolve(url).func.view_class, HorariosView)

    def test_create_url_horarios(self):
        url = reverse('centroidiomas:horarios_create')
        self.assertEquals(resolve(url).func.view_class, HorariosCreateView)

    def test_update_url_horarios(self):
        url = reverse('centroidiomas:horarios_update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, HorariosUpdateView)

    def test_delete_url_horarios(self):
        url = reverse('centroidiomas:horarios_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, HorariosDeleteView)

    #Test url idiomas
    def test_list_url_idioma(self):
        url = reverse('centroidiomas:idioma_view')
        self.assertEquals(resolve(url).func.view_class, IdiomaView)

    def test_create_url_idioma(self):
        url = reverse('centroidiomas:idioma_create')
        self.assertEquals(resolve(url).func.view_class, IdiomaCreateView)

    def test_update_url_idioma(self):
        url = reverse('centroidiomas:idioma_update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, IdiomaUpdateView)

    def test_delete_url_idioma(self):
        url = reverse('centroidiomas:idioma_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, IdiomaDeleteView)


    #Test url inscripcion
    def test_list_url_inscripcion(self):
        url = reverse('centroidiomas:inscripcion_view')
        self.assertEquals(resolve(url).func.view_class, InscripcionView)

    def test_create_url_inscripcion(self):
        url = reverse('centroidiomas:inscripcion_create')
        self.assertEquals(resolve(url).func.view_class, InscripcionCreateView)

    def test_update_url_inscripcion(self):
        url = reverse('centroidiomas:inscripcion_update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, InscripcionUpdateView)

    def test_delete_url_inscripcion(self):
        url = reverse('centroidiomas:inscripcion_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, InscripcionDeleteView)


    #Test url niveles
    def test_list_url_niveles(self):
        url = reverse('centroidiomas:niveles_view')
        self.assertEquals(resolve(url).func.view_class, NivelesView)

    def test_create_url_niveles(self):
        url = reverse('centroidiomas:niveles_create')
        self.assertEquals(resolve(url).func.view_class, NivelesCreateView)

    def test_update_url_niveles(self):
        url = reverse('centroidiomas:niveles_update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, NivelesUpdateView)

    def test_delete_url_niveles(self):
        url = reverse('centroidiomas:niveles_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, NivelesDeleteView)


    #Test url salon
    def test_list_url_salon(self):
        url = reverse('centroidiomas:salon_view')
        self.assertEquals(resolve(url).func.view_class, SalonView)

    def test_create_url_salon(self):
        url = reverse('centroidiomas:salon_create')
        self.assertEquals(resolve(url).func.view_class, SalonCreateView)

    def test_update_url_salon(self):
        url = reverse('centroidiomas:salon_update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, SalonUpdateView)

    def test_delete_url_salon(self):
        url = reverse('centroidiomas:salon_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, SalonDeleteView)
