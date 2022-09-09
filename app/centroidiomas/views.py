from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView

from app.centroidiomas.forms import SalonForm, PeriodoAcademicoForm, NivelesForm, InscripcionForm, IdiomaForm, \
    HorariosForm, GruposForm, ConvocatoriaInsForm, AspiranteForm, AspiranteCreateForm, InscripcionAspiranteForm
from app.centroidiomas.models import Salon, Niveles, Inscripcion, Idioma, Horarios, Grupos, Aspirante, Periodoacademico, \
    Convocatoriainscripcion


class AspiranteView(ListView):
    model = Aspirante
    queryset = model.objects.all()
    template_name = 'aspirante/list_aspirante.html'

    def get_context_data(self, **kwargs):
        context = super(AspiranteView, self).get_context_data(**kwargs)
        context['location'] = 'Listado aspirantes'
        context['message_help'] = 'Listado en el que encontraras todos los aspirantes a cursar un idioma'
        return context


class AspiranteCreateView(CreateView):
    model = Aspirante
    form_class = AspiranteForm
    success_url = reverse_lazy('centroidiomas:aspirante_view')
    template_name = 'aspirante/aspirante_form.html'

    def get_context_data(self, **kwargs):
        context = super(AspiranteCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Creación de aspirante'
        context['title'] = 'Crear aspirante'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            try:
                form.save()
                messages.success(request, 'Creado correctamente!')
                return redirect(self.success_url)
            except ValueError as e:
                pass
        else:
            form = AspiranteForm()
            messages.error(request, 'El correo electronico ya existe')
            return render(request, self.template_name, {'form': form})


class AspiranteUpdateView(UpdateView):
    model = Aspirante
    form_class = AspiranteForm
    context_object_name = 'obj'
    success_url = reverse_lazy('centroidiomas:aspirante_view')
    template_name = 'aspirante/aspirante_form.html'

    def get_context_data(self, **kwargs):
        context = super(AspiranteUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar aspirante'
        context['title'] = 'Actualizar aspirante'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs.get('pk')
        aspirante = self.model.objects.get(aspi_id=pk)
        form = self.form_class(request.POST, instance=aspirante)
        if form.is_valid():
            form.save(commit=False)
            try:
                email = form.cleaned_data.get('aspi_correo')
                email_validate = Aspirante.objects.filter(aspi_correo=email)
                if not email_validate:
                    form.save()
                    messages.success(request, 'Actualizado correctamente!')
                    return redirect(self.success_url)
            except ValueError as e:
                pass
        else:
            messages.error(request, 'El correo electronico ya existe')
            return redirect(reverse_lazy('centroidiomas:aspirante_update', kwargs={'pk': pk}))


class AspiranteDeleteView(DeleteView):
    model = Aspirante
    success_url = reverse_lazy('centroidiomas:aspirante_view')
    template_name = 'aspirante/aspirante_delete.html'

    def get_context_data(self, **kwargs):
        context = super(AspiranteDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar aspirante'
        context['title'] = 'Eliminar aspirante'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        aspirante = Aspirante.objects.get(aspi_id=kwargs['pk'])
        try:
            if aspirante:
                aspirante.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect(self.success_url)
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:aspirante_delete', kwargs={'pk': pk}))


class ConvocatoriaInsView(ListView):
    model = Convocatoriainscripcion
    queryset = model.objects.all()
    template_name = 'convocatoriainscripcion/list_convoins.html'

    def get_context_data(self, **kwargs):
        context = super(ConvocatoriaInsView, self).get_context_data(**kwargs)
        context['location'] = 'Listado convocatorias'
        context['message_help'] = 'Listado en el que encontraras todas las convocatorias'
        return context


class ConvocatoriaInsCreateView(CreateView):
    model = Convocatoriainscripcion
    form_class = ConvocatoriaInsForm
    success_url = reverse_lazy('centroidiomas:convocatoriainscripcion_view')
    template_name = 'convocatoriainscripcion/convoins_form.html'

    def get_context_data(self, **kwargs):
        context = super(ConvocatoriaInsCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Creación de convocatoria'
        context['title'] = 'Crear convocatoria'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            try:
                fecha1 = form.cleaned_data.get('coin_fechainicio')
                fecha2 = form.cleaned_data.get('coin_fechafin')
                if fecha1 < fecha2:
                    form.save()
                    messages.success(request, 'Creado correctamente!')
                    return redirect(self.success_url)
            except ValueError as e:
                pass
        else:
            form = ConvocatoriaInsForm()
            messages.error(request, 'La fecha de inicio no puede ser mayor o igual a la de finalización')
            return render(request, self.template_name, {'form': form})


class ConvocatoriaInsUpdateView(UpdateView):
    model = Convocatoriainscripcion
    form_class = ConvocatoriaInsForm
    success_url = reverse_lazy('centroidiomas:convocatoriainscripcion_view')
    context_object_name = 'obj'
    template_name = 'convocatoriainscripcion/convoins_form.html'

    def get_context_data(self, **kwargs):
        context = super(ConvocatoriaInsUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar convocatoria'
        context['title'] = 'Actualizar convocatoria'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs.get('pk')
        convocatoria = self.model.objects.get(coin_id=pk)
        form = self.form_class(request.POST, instance=convocatoria)
        if form.is_valid():
            form.save(commit=False)
            try:
                fecha1 = form.cleaned_data.get('coin_fechainicio')
                fecha2 = form.cleaned_data.get('coin_fechafin')
                if fecha1 < fecha2:
                    form.save()
                    messages.success(request, 'Actualizado correctamente!')
                    return redirect(self.success_url)
            except ValueError as e:
                pass
        else:
            messages.error(request, 'La fecha de inicio no puede ser mayor a la de finalización')
            return redirect(reverse_lazy('centroidiomas:convocatoriainscripcion_update', kwargs={'pk': pk}))


class ConvocatoriaInsDeleteView(DeleteView):
    model = Convocatoriainscripcion
    success_url = reverse_lazy('centroidiomas:convocatoriainscripcion_view')
    template_name = 'convocatoriainscripcion/convoins_delete.html'

    def get_context_data(self, **kwargs):
        context = super(ConvocatoriaInsDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar convocatoria'
        context['title'] = 'Eliminar convocatoria'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        convocatoria = Convocatoriainscripcion.objects.get(coin_id=kwargs['pk'])
        try:
            if convocatoria:
                convocatoria.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect(self.success_url)
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:convocatoriainscripcion_delete', kwargs={'pk': pk}))


class GruposView(ListView):
    model = Grupos
    queryset = Grupos.objects.all()
    template_name = 'grupos/list_grupos.html'

    def get_context_data(self, **kwargs):
        context = super(GruposView, self).get_context_data(**kwargs)
        context['location'] = 'Listado grupos de estudiantes'
        context['message_help'] = 'Listado en el que encontraras todos los grupos de estudiantes'
        return context


class GruposCreateView(CreateView):
    model = Grupos
    form_class = GruposForm
    success_url = reverse_lazy('centroidiomas:grupos_view')
    template_name = 'grupos/grupos_form.html'

    def get_context_data(self, **kwargs):
        context = super(GruposCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Crear grupos de estudiantes'
        context['title'] = 'Crear grupo'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            grupos = Grupos.objects.filter(grup_nombre=form.cleaned_data.get('grup_nombre'))
            if grupos:
                messages.error(request, 'El nombre del grupo ya existe')
                return redirect('centroidiomas:grupos_create')
            form.save()
            messages.success(request, 'Creado correctamente')
            return redirect(self.success_url)
        else:
            form = GruposForm()
            return render(request, self.template_name, {'form': form})


class GruposUpdateView(UpdateView):
    model = Grupos
    template_name = 'grupos/grupos_form.html'
    form_class = GruposForm
    context_object_name = 'obj'
    success_url = reverse_lazy('centroidiomas:grupos_view')

    def get_context_data(self, **kwargs):
        context = super(GruposUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar grupos de estudiantes'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs.get('pk')
        grupos = self.model.objects.get(grup_id=pk)
        form = self.form_class(request.POST, instance=grupos)
        if form.is_valid():
            form.save(commit=False)
            grupos = Grupos.objects.filter(grup_nombre=request.POST['grup_nombre'])
            if grupos:
                messages.error(request, 'El nombre del grupo ya existe')
                return redirect(reverse_lazy('centroidiomas:grupos_update', kwargs={'pk': pk}))
            form.save()
            messages.success(request, 'Actualizado correctamente')
            return redirect(self.success_url)


class GruposDeleteView(DeleteView):
    model = Grupos
    success_url = reverse_lazy('centroidiomas:grupos_view')
    template_name = 'grupos/grupos_delete.html'

    def get_context_data(self, **kwargs):
        context = super(GruposDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar grupos de estudiantes'
        context['title'] = 'Eliminar grupo'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        grupos = Grupos.objects.get(grup_id=kwargs['pk'])
        try:
            if grupos:
                grupos.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect(self.success_url)
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:grupos_delete', kwargs={'pk': pk}))


class HorariosView(ListView):
    model = Horarios
    queryset = Horarios.objects.all()
    template_name = 'horarios/list_horarios.html'

    def get_context_data(self, **kwargs):
        context = super(HorariosView, self).get_context_data(**kwargs)
        context['location'] = 'Horarios de los idiomas'
        context['message_help'] = 'Listado en el que encontraras el listado de los horarios asignado a los grupos'
        return context


class HorariosCreateView(CreateView):
    model = Horarios
    form_class = HorariosForm
    success_url = reverse_lazy('centroidiomas:horarios_view')
    template_name = 'horarios/horarios_form.html'

    def get_context_data(self, **kwargs):
        context = super(HorariosCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Crear horario de los idiomas'
        context['title'] = 'Crear horarios'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, 'Creado correctamente')
            return redirect(self.success_url)


class HorariosUpdateView(UpdateView):
    model = Horarios
    template_name = 'horarios/horarios_form.html'
    form_class = HorariosForm
    context_object_name = 'obj'
    success_url = reverse_lazy('centroidiomas:horarios_view')

    def get_context_data(self, **kwargs):
        context = super(HorariosUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar horario de los idiomas'
        context['title'] = 'Actualizar horarios'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs.get('pk')
        horario = self.model.objects.get(hora_id=pk)
        form = self.form_class(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Actualizado correctamente!')
            return redirect('centroidiomas:horarios_view')


class HorariosDeleteView(DeleteView):
    model = Horarios
    success_url = reverse_lazy('centroidiomas:horarios_view')
    template_name = 'horarios/horarios_delete.html'

    def get_context_data(self, **kwargs):
        context = super(HorariosDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar horario de los idiomas'
        context['title'] = 'Eliminar horarios'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        horario = Horarios.objects.get(hora_id=kwargs['pk'])
        try:
            if horario:
                horario.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect('centroidiomas:horarios_view')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:horarios_delete', kwargs={'pk': pk}))


class IdiomaView(ListView):
    model = Idioma
    queryset = Idioma.objects.all()
    template_name = 'idioma/list_idioma.html'

    def get_context_data(self, **kwargs):
        context = super(IdiomaView, self).get_context_data(**kwargs)
        context['location'] = 'Listado de idiomas disponibles'
        context['message_help'] = 'Listado en el que encontraras los idiomas activos e inactivos'
        return context


class IdiomaCreateView(CreateView):
    model = Idioma
    form_class = IdiomaForm
    success_url = reverse_lazy('centroidiomas:idioma_view')
    template_name = 'idioma/idioma_form.html'

    def get_context_data(self, **kwargs):
        context = super(IdiomaCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Crear idioma'
        context['title'] = 'Crear idioma'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            idioma = Idioma.objects.filter(idio_nombre=form.cleaned_data.get('idio_nombre'))
            if idioma:
                messages.error(request, 'El nombre del idioma ya existe')
                return redirect('centroidiomas:idioma_create')
            form.save()
            messages.success(request, 'Creado correctamente')
            return redirect(self.success_url)
        else:
            form = NivelesForm()
            return render(request, self.template_name, {'form': form})


class IdiomaUpdateView(UpdateView):
    model = Idioma
    template_name = 'idioma/idioma_form.html'
    form_class = IdiomaForm
    context_object_name = 'obj'
    success_url = reverse_lazy('centroidiomas:idioma_view')

    def get_context_data(self, **kwargs):
        context = super(IdiomaUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar idioma'
        context['title'] = 'Actualizar idioma'
        return context


class IdiomaDeleteView(DeleteView):
    model = Idioma
    success_url = reverse_lazy('centroidiomas:idioma_view')
    template_name = 'idioma/idioma_delete.html'

    def get_context_data(self, **kwargs):
        context = super(IdiomaDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar idioma'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        idioma = self.model.objects.get(idio_id=kwargs['pk'])
        try:
            if idioma:
                idioma.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect('centroidiomas:idioma_view')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:idioma_delete', kwargs={'pk': pk}))


class InscripcionView(ListView):
    model = Inscripcion
    queryset = Inscripcion.objects.all()
    template_name = 'inscripcion/list_inscripcion.html'

    def get_context_data(self, **kwargs):
        context = super(InscripcionView, self).get_context_data(**kwargs)
        context['location'] = 'Inscripción'
        context['message_help'] = 'Listado en el que encontraras las inscripciones realizadas'
        return context


class InscripcionCreateView(CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    success_url = reverse_lazy('centroidiomas:inscripcion_view')
    template_name = 'inscripcion/inscripcion_form.html'

    def get_context_data(self, **kwargs):
        context = super(InscripcionCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Crear inscripción'
        context['title'] = 'Crear inscripción'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Creado correctamente')
            return redirect('centroidiomas:inscripcion_view')


class InscripcionUpdateView(UpdateView):
    model = Inscripcion
    template_name = 'inscripcion/inscripcion_form.html'
    form_class = InscripcionForm
    context_object_name = 'obj'
    success_url = reverse_lazy('centroidiomas:inscripcion_view')

    def get_context_data(self, **kwargs):
        context = super(InscripcionUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar inscripción'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs.get('pk')
        inscripcion = self.model.objects.get(insc_id=pk)
        form = self.form_class(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Actualizado correctamente!')
            return redirect('centroidiomas:inscripcion_view')


class InscripcionDeleteView(DeleteView):
    model = Inscripcion
    success_url = reverse_lazy('centroidiomas:inscripcion_view')
    template_name = 'inscripcion/inscripcion_delete.html'

    def get_context_data(self, **kwargs):
        context = super(InscripcionDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar inscripción'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        inscripcion = Inscripcion.objects.get(insc_id=kwargs['pk'])
        try:
            if inscripcion:
                inscripcion.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect('centroidiomas:inscripcion_view')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:inscripcion_delete', kwargs={'pk': pk}))


class NivelesView(ListView):
    model = Niveles
    queryset = Niveles.objects.all()
    template_name = 'niveles/list_niveles.html'

    def get_context_data(self, **kwargs):
        context = super(NivelesView, self).get_context_data(**kwargs)
        context['location'] = 'Niveles de los idiomas'
        context['message_help'] = 'Listado en el que encontraras los niveles de cada curso'
        return context


class NivelesCreateView(CreateView):
    model = Niveles
    form_class = NivelesForm
    template_name = 'niveles/niveles_form.html'
    success_url = reverse_lazy('centroidiomas:niveles_view')

    def get_context_data(self, **kwargs):
        context = super(NivelesCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Crear niveles de los idiomas'
        context['title'] = 'Crear niveles'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            nivel = Niveles.objects.filter(nive_nombre=form.cleaned_data.get('nive_nombre'))
            if nivel:
                messages.error(request, 'El nombre del nivel ya existe')
                return redirect('centroidiomas:niveles_create')
            form.save()
            messages.success(request, 'Creado correctamente')
            return redirect('centroidiomas:niveles_view')
        else:
            form = NivelesForm()
            return render(request, self.template_name, {'form': form})


class NivelesUpdateView(UpdateView):
    model = Niveles
    template_name = 'niveles/niveles_form.html'
    form_class = NivelesForm
    context_object_name = 'obj'
    success_url = reverse_lazy('centroidiomas:niveles_view')

    def get_context_data(self, **kwargs):
        context = super(NivelesUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar niveles de los idiomas'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs.get('pk')
        nivel = self.model.objects.get(nive_id=pk)
        form = self.form_class(request.POST, instance=nivel)
        if form.is_valid():
            form.save(commit=False)
            nivel = Niveles.objects.filter(nive_nombre=request.POST['nive_nombre'])
            if nivel:
                messages.error(request, 'El nombre del nivel ya existe')
                return redirect(reverse_lazy('centroidiomas:niveles_update', kwargs={'pk': pk}))
            form.save()
            messages.success(request, 'Actualizado correctamente')
            return redirect('centroidiomas:salon_view')


class NivelesDeleteView(DeleteView):
    model = Niveles
    success_url = reverse_lazy('centroidiomas:niveles_view')
    template_name = 'niveles/niveles_delete.html'

    def get_context_data(self, **kwargs):
        context = super(NivelesDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar niveles de los idiomas'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        nivel = self.model.objects.get(nive_id=kwargs['pk'])
        try:
            if nivel:
                nivel.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect('centroidiomas:niveles_view')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:niveles_delete', kwargs={'pk': pk}))


class PeriodoAcademicoView(ListView):
    model = Periodoacademico
    queryset = model.objects.all()
    template_name = 'periodoacademico/list_periodoacademico.html'

    def get_context_data(self, **kwargs):
        context = super(PeriodoAcademicoView, self).get_context_data(**kwargs)
        context['location'] = 'Periodo academico'
        context['message_help'] = 'Listado de los periodos academicos'
        return context


class PeriodoAcademicoCreateView(CreateView):
    model = Periodoacademico
    form_class = PeriodoAcademicoForm
    template_name = 'periodoacademico/periodoacademico_form.html'
    success_url = reverse_lazy('centroidiomas:periodoacademico_view')

    def get_context_data(self, **kwargs):
        context = super(PeriodoAcademicoCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Crear los periodos academicos'
        context['title'] = 'Crear periodo academico'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            try:
                fecha1 = form.cleaned_data.get('peac_fechainicio')
                fecha2 = form.cleaned_data.get('peac_fechafin')
                if fecha1 < fecha2:
                    form.save()
                    messages.success(request, 'Creado correctamente!')
                    return redirect(self.success_url)
            except ValueError as e:
                pass
        else:
            form = PeriodoAcademicoForm()
            messages.error(request, 'La fecha de inicio no puede ser mayor a la de finalización')
            return render(request, self.template_name, {'form': form})


class PeriodoAcademicoUpdateView(UpdateView):
    model = Periodoacademico
    template_name = 'periodoacademico/periodoacademico_form.html'
    form_class = PeriodoAcademicoForm
    context_object_name = 'obj'
    success_url = reverse_lazy('centroidiomas:periodoacademico_view')

    def get_context_data(self, **kwargs):
        context = super(PeriodoAcademicoUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar periodo academico'
        context['title'] = 'Actualizar periodo academico'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs.get('pk')
        peraca = self.model.objects.get(peac_id=pk)
        form = self.form_class(request.POST, instance=peraca)
        if form.is_valid():
            form.save(commit=False)
            try:
                fecha1 = form.cleaned_data.get('peac_fechainicio')
                fecha2 = form.cleaned_data.get('peac_fechafin')
                if fecha1 < fecha2:
                    form.save()
                    messages.success(request, 'Actualizado correctamente!')
                    return redirect('centroidiomas:periodoacademico_view')
            except ValueError as e:
                pass
        else:
            messages.error(request, 'La fecha de inicio no puede ser mayor a la de finalización')
            return redirect(reverse_lazy('centroidiomas:periodoacademico_update', kwargs={'pk': pk}))


class PeriodoAcademicoDeleteView(DeleteView):
    model = Periodoacademico
    success_url = reverse_lazy('centroidiomas:periodoacademico_view')
    template_name = 'periodoacademico/periodoacademico_delete.html'

    def get_context_data(self, **kwargs):
        context = super(PeriodoAcademicoDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar periodo academico'
        context['title'] = 'Eliminar periodo academico'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        peraca = Periodoacademico.objects.get(peac_id=kwargs['pk'])
        try:
            if peraca:
                peraca.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect('centroidiomas:periodoacademico_view')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:periodoacademico_delete', kwargs={'pk': pk}))


class SalonView(ListView):
    model = Salon
    queryset = model.objects.all()
    template_name = 'salon/list_salones.html'

    def get_context_data(self, **kwargs):
        context = super(SalonView, self).get_context_data(**kwargs)
        context['location'] = 'Salones para los idiomas'
        context['message_help'] = 'Listado de los salones disponibles para dictar los cursos'
        return context


class SalonCreateView(CreateView):
    model = Salon
    form_class = SalonForm
    template_name = 'salon/salon_form.html'
    success_url = reverse_lazy('centroidiomas:salon_view')

    def get_context_data(self, **kwargs):
        context = super(SalonCreateView, self).get_context_data(**kwargs)
        context['location'] = 'Asignar salones a los idiomas'
        context['title'] = 'Crear salones'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            salon = Salon.objects.filter(salo_nombre=form.cleaned_data.get('salo_nombre'))
            if salon:
                messages.error(request, 'El salon ya existe')
                return redirect('centroidiomas:salon_create')
            form.save()
            messages.success(request, 'Creado correctamente')
            return redirect('centroidiomas:salon_view')
        else:
            form = SalonForm()
            return render(request, self.template_name, {'form': form})


class SalonUpdateView(UpdateView):
    model = Salon
    template_name = 'salon/salon_form.html'
    form_class = SalonForm
    context_object_name = 'obj'
    success_url = reverse_lazy('centroidiomas:salon_view')

    def get_context_data(self, **kwargs):
        context = super(SalonUpdateView, self).get_context_data(**kwargs)
        context['location'] = 'Actualizar salones para los idiomas'
        context['title'] = 'Actualizar salon'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs.get('pk')
        salon = self.model.objects.get(salo_id=pk)
        form = self.form_class(request.POST, instance=salon)
        if form.is_valid():
            form.save(commit=False)
            salon = Salon.objects.filter(salo_nombre=request.POST['salo_nombre'])
            if salon:
                messages.error(request, 'El salon ya existe')
                return redirect(reverse_lazy('centroidiomas:salon_update', kwargs={'pk': pk}))
            form.save()
            messages.success(request, 'Actualizado correctamente')
            return redirect('centroidiomas:salon_view')


class SalonDeleteView(DeleteView):
    model = Salon
    success_url = reverse_lazy('centroidiomas:salon_view')
    template_name = 'salon/salon_delete.html'

    def get_context_data(self, **kwargs):
        context = super(SalonDeleteView, self).get_context_data(**kwargs)
        context['location'] = 'Eliminar salones para los idiomas'
        context['title'] = 'Eliminar salon'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        self.object = self.get_object
        salon = Salon.objects.get(salo_id=kwargs['pk'])
        try:
            if salon:
                salon.delete()
                messages.success(request, 'Eliminado correctamente')
                return redirect('centroidiomas:salon_view')
        except Exception as e:
            messages.error(request, 'No se puede eliminar el registro')
            return redirect(reverse_lazy('centroidiomas:salon_delete', kwargs={'pk': pk}))


class CreateAspiranteView(CreateView):
    model = Aspirante
    form_class = AspiranteCreateForm
    template_name = 'aspirantetemplate/create_aspirante.html'

    def get_context_data(self, **kwargs):
        context = super(CreateAspiranteView, self).get_context_data(**kwargs)
        context['title'] = 'Ingresa tus datos'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=False)
            solicitud = Aspirante.objects.create(
            aspi_primernombre=form.cleaned_data.get('aspi_primernombre'),
            aspi_segundonombre=form.cleaned_data.get('aspi_segundonombre'),
            aspi_primerapellido=form.cleaned_data.get('aspi_primerapellido'),
            aspi_segundoapellido=form.cleaned_data.get('aspi_segundoapellido'),
            aspi_correo=form.cleaned_data.get('aspi_correo'),
            aspi_genero=form.cleaned_data.get('aspi_genero'),
            tipodocumento_id=form.cleaned_data.get('tipodocumento_id'),
            aspi_numerodocumento=form.cleaned_data.get('aspi_numerodocumento'),
            aspi_rh=form.cleaned_data.get('aspi_rh'),
            aspi_numerocelular=form.cleaned_data.get('aspi_numerocelular'),
            aspi_telefonocasa=form.cleaned_data.get('aspi_telefonocasa'),
            aspi_estado='aspirante',
            aspi_ciudadnacimiento=form.cleaned_data.get('aspi_ciudadnacimiento'),
            aspi_ciudadexpediciondocumento=form.cleaned_data.get('aspi_ciudadexpediciondocumento'),
            aspi_ciudadresidencia=form.cleaned_data.get('aspi_ciudadresidencia'),
            aspi_direccion=form.cleaned_data.get('aspi_direccion'),
            )
            request.session['id_aspirante'] = solicitud.aspi_id
            messages.success(request, 'Creado correctamente!')
            return redirect(reverse_lazy('centroidiomas:aspiranteconvocatoriainscripcion_view'))
        else:
            form = AspiranteCreateForm()
            messages.error(request, 'El correo electronico ya existe')
            return render(request, self.template_name, {'form': form})


class ConvocatoriaAspiranteInsView(ListView):
    model = Convocatoriainscripcion
    queryset = model.objects.all()
    template_name = 'aspirantetemplate/list_convocatorias.html'

    def get_context_data(self, **kwargs):
        context = super(ConvocatoriaAspiranteInsView, self).get_context_data(**kwargs)
        context['sesiion'] = self.request.session['id_aspirante']
        context['location'] = 'Listado convocatorias'
        context['message_help'] = 'Listado en el que encontraras todas las convocatorias'
        return context


def InscripcionAspiranteCreate(request):
    pk = request.POST
    Inscripcion.objects.create(
        insc_estadoinscripcion='inscrito',
        aspirante=Aspirante.objects.get(aspi_id=request.session['id_aspirante']),
        insc_fechainscripcion=timezone.now().date(),
        grupos=Grupos.objects.all().first(),
        idioma=Idioma.objects.get(idio_id=pk['idioma'])
    )
    messages.success(request, 'Inscrito correctamente')
    return redirect(reverse_lazy('centroidiomas:aspiranteconvocatoriainscripcion_view'))
