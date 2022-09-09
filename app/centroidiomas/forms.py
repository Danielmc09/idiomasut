from django import forms

from app.centroidiomas.models import Salon, Periodoacademico, Niveles, Inscripcion, Idioma, Horarios, Grupos, \
    Convocatoriainscripcion, Aspirante


class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ['salo_nombre', 'salo_bloque']
        labels = {
            'salo_nombre': 'Nombre del salon :',
            'salo_bloque': 'Nombre bloque :',
        }
        widgets = {
            'salo_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre del salon',
                    'id': 'salo_nombre'
                }
            ),
            'salo_bloque': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre del bloque',
                    'id': 'salo_bloque'
                }
            )
        }

    def clean_salo_nombre(self):
        salon_nombre = self.cleaned_data.get('salo_nombre')
        if len(salon_nombre) > 100:
            raise forms.ValidationError('El campo no puede ser mayor a 100 caracteres')
        return salon_nombre

    def clean_salo_bloque(self):
        salon_bloque = self.cleaned_data.get('salo_bloque')
        if len(salon_bloque) > 100:
            raise forms.ValidationError('El campo no puede ser mayor a 100 caracteres')
        return salon_bloque

class PeriodoAcademicoForm(forms.ModelForm):
    class Meta:
        model = Periodoacademico
        fields = ['peac_fechainicio', 'peac_fechafin', 'peac_ano', 'peac_descripcion']
        labels = {
            'peac_fechainicio': 'Fecha de inicio :',
            'peac_fechafin': 'Fecha finalización :',
            'peac_ano': 'Año :',
            'peac_descripcion': 'Descripción :',
        }
        widgets = {
            'peac_fechainicio': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la fecha de inicio',
                    'id': 'peac_fechainicio',
                    'type': 'date'
                }
            ),
            'peac_fechafin': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la fecha de finalización',
                    'id': 'peac_fechafin',
                    'type': 'date'
                }
            ),
            'peac_ano': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el año',
                    'id': 'peac_ano',
                    'type': 'date'
                }
            ),
            'peac_descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa una descripción',
                    'id': 'peac_descripcion'
                }
            )
        }

    def clean_peac_fechafin(self):
        peac_fechainicio = self.cleaned_data.get('peac_fechainicio')
        peac_fechafin = self.cleaned_data.get('peac_fechafin')
        if peac_fechainicio >= peac_fechafin:
            raise forms.ValidationError('La fecha de inicio no puede ser mayor a la fecha de finalización')
        return peac_fechafin


class NivelesForm(forms.ModelForm):
    class Meta:
        model = Niveles
        fields = ['nive_nombre', 'nive_numeronivel', 'nive_duracion', 'nive_descripcion',
                  'nive_code']
        labels = {
            'nive_nombre': 'Nombre del nivel :',
            'nive_numeronivel': 'Número del nivel :',
            'nive_duracion': 'Duración del nivel :',
            'nive_descripcion': 'Descripción del nivel :',
            'nive_code': 'Código del nivel :',
        }
        widgets = {
            'nive_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre del nivel del idioma',
                    'id': 'nive_nombre'
                }
            ),
            'nive_numeronivel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el número del nivel',
                    'id': 'nive_numeronivel'
                }
            ),
            'nive_duracion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la duración del nivel',
                    'id': 'nive_duracion'
                }
            ),
            'nive_descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa una descripción del nivel',
                    'id': 'nive_descripcion'
                }
            ),
            'nive_code': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el código del nivel',
                    'id': 'nive_code'
                }
            )
        }


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['insc_estadoinscripcion', 'aspirante', 'insc_fechainscripcion', 'grupos',
                  'idioma']
        labels = {
            'insc_estadoinscripcion': 'Estado inscripción :',
            'aspirante': 'Aspirante :',
            'insc_fechainscripcion': 'Fecha inscripción :',
            'grupos': 'Grupos :',
            'idioma': 'Idioma :',
        }
        widgets = {
            'insc_estadoinscripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese estado de la inscripción',
                    'id': 'insc_estadoinscripcion'
                }
            ),
            'aspirante': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el número del nivel',
                    'id': 'aspirante'
                }
            ),
            'insc_fechainscripcion': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la duración del nivel',
                    'id': 'insc_fechainscripcion'
                }
            ),
            'grupos': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione grupo',
                    'id': 'grupos'
                }
            ),
            'idioma': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione el idioma',
                    'id': 'idioma'
                }
            )
        }


class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = ['idio_nombre', 'idio_descripcion', 'idio_estado', 'niveles']
        labels = {
            'idio_nombre': 'Nombre del idioma :',
            'idio_descripcion': 'Descripción del idioma :',
            'idio_estado': 'Estado idioma :',
            'niveles': 'Niveles :',
        }
        widgets = {
            'idio_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del idioma',
                    'id': 'idio_nombre'
                }
            ),
            'idio_descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa una breve descripción',
                    'id': 'idio_descripcion'
                }
            ),
            'idio_estado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el estado del idioma',
                    'id': 'idio_estado'
                }
            ),
            'niveles': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione idioma',
                    'id': 'niveles'
                }
            )
        }


class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = ['hora_horario', 'salon', 'grupos']
        labels = {
            'hora_horario': 'Horario :',
            'salon': 'Selecciona el salon :',
            'grupos': 'Selecciona el grupo :',
        }
        widgets = {
            'hora_horario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el horario del grupo',
                    'id': 'hora_horario'
                }
            ),
            'salon': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecciona el salon',
                    'id': 'salon'
                }
            ),
            'grupos': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecciona el grupo',
                    'id': 'grupos'
                }
            )
        }


class GruposForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['grup_nombre', 'grup_descripcion', 'grup_cantidad', 'niveles']
        labels = {
            'grup_nombre': 'Nombre del grupo :',
            'grup_descripcion': 'Descripción del grupo :',
            'grup_cantidad': 'Cantidad de alumnos :',
            'niveles': 'Nivel : :',
        }
        widgets = {
            'grup_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el horario del grupo',
                    'id': 'grup_nombre'
                }
            ),
            'grup_descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una breve descripción',
                    'id': 'grup_descripcion'
                }
            ),
            'grup_cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecciona el grupo',
                    'id': 'grup_cantidad'
                }
            ),
            'niveles': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecciona el nivel',
                    'id': 'niveles'
                }
            )
        }


class ConvocatoriaInsForm(forms.ModelForm):
    class Meta:
        model = Convocatoriainscripcion
        fields = ['inscripcion', 'idioma', 'coin_fechainicio', 'coin_fechafin', 'coin_nombre',
                  'coin_numerocupos', 'periodoacademico']
        labels = {
            'inscripcion': 'Inscripción :',
            'idioma': 'Idioma :',
            'coin_fechainicio': 'Fecha de inicio :',
            'coin_fechafin': 'Fecha finalización :',
            'coin_nombre': 'Nombre convocatoria :',
            'coin_numerocupos': 'Número de cupos convocatoria :',
            'periodoacademico': 'Periodo academico :',
        }
        widgets = {
            'inscripcion': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'inscripcion'
                }
            ),
            'idioma': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'idioma'
                }
            ),
            'coin_fechainicio': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'id': 'coin_fechainicio'
                }
            ),
            'coin_fechafin': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'id': 'coin_fechafin'
                }
            ),
            'coin_nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa el nombre de la convocatoria',
                    'id': 'coin_nombre'
                }
            ),
            'coin_numerocupos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la cantidad de cupos',
                    'id': 'coin_numerocupos'
                }
            ),
            'periodoacademico': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'periodoacademico'
                }
            )
        }

    def clean_coin_fechafin(self):
        coin_fechainicio = self.cleaned_data.get('coin_fechainicio')
        coin_fechafin = self.cleaned_data.get('coin_fechafin')
        if coin_fechainicio >= coin_fechafin:
            raise forms.ValidationError('La fecha de inicio no puede ser mayor a la fecha de finalización')
        return coin_fechafin

class AspiranteForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = ['aspi_primernombre', 'aspi_segundonombre', 'aspi_primerapellido',
                  'aspi_segundoapellido', 'aspi_correo', 'aspi_genero', 'tipodocumento_id',
                  'aspi_numerodocumento', 'aspi_rh', 'aspi_numerocelular', 'aspi_telefonocasa',
                  'aspi_estado', 'aspi_ciudadnacimiento', 'aspi_ciudadexpediciondocumento',
                  'aspi_ciudadresidencia', 'aspi_direccion']
        labels = {
            'aspi_primernombre': 'Ingrese su primer nombre',
            'aspi_segundonombre': 'Ingrese su segundo nombre',
            'aspi_primerapellido': 'Ingrese su primer apellido',
            'aspi_segundoapellido': 'Ingrese su segundo apellido',
            'aspi_correo': 'Igrese su correo electronico',
            'aspi_genero': 'Seleccione su genero',
            'tipodocumento_id': 'Tipo de documento',
            'aspi_numerodocumento': 'Número de documento',
            'aspi_rh': 'Selecciones su RH+',
            'aspi_numerocelular': 'Ingrese su número de celular',
            'aspi_telefonocasa': 'Ingrese el número fijo de su casa',
            'aspi_estado': 'estado aspirante',
            'aspi_ciudadnacimiento': 'Seleccione la ciudad de nacimiento',
            'aspi_ciudadexpediciondocumento': 'Seleccione la ciudad de expedicion de documento',
            'aspi_ciudadresidencia': 'Seleccione la ciudad de residencia',
            'aspi_direccion': 'Ingrese la dirección de residencia',
        }


        widgets = {
            'aspi_primernombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa primer nombre',
                    'id': 'aspi_primernombre'
                }
            ),
            'aspi_segundonombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa segundo nombre',
                    'id': 'aspi_segundonombre'
                }
            ),
            'aspi_primerapellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa primer apellido',
                    'id': 'aspi_primerapellido'
                }
            ),
            'aspi_segundoapellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa segundo apellido',
                    'id': 'aspi_segundoapellido'
                }
            ),
            'aspi_correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa su correo electronico',
                    'id': 'aspi_correo'
                }
            ),
            'aspi_genero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione genero',
                    'id': 'aspi_genero'
                }
            ),
            'tipodocumento_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione tipo de documento',
                    'id': 'tipodocumento_id'
                }
            ),
            'aspi_numerodocumento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de documento',
                    'id': 'aspi_numerodocumento'
                }
            ),
            'aspi_rh': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su RH+',
                    'id': 'aspi_rh'
                }
            ),
            'aspi_numerocelular': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de celular',
                    'id': 'aspi_numerocelular'
                }
            ),
            'aspi_telefonocasa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de telefono fijo',
                    'id': 'aspi_telefonocasa'
                }
            ),
            'aspi_estado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estado aspirante',
                    'id': 'aspi_estado'
                }
            ),
            'aspi_ciudadnacimiento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione su ciudad de nacimiento',
                    'id': 'aspi_ciudadnacimiento'
                }
            ),
            'aspi_ciudadexpediciondocumento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione la ciudad de expedición de su documento',
                    'id': 'aspi_ciudadexpediciondocumento'
                }
            ),
            'aspi_ciudadresidencia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione su ciudad de residencia',
                    'id': 'aspi_ciudadresidencia'
                }
            ),
            'aspi_direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección de su residencia',
                    'id': 'aspi_direccion'
                }
            )
        }

    def clean_aspi_correo(self):
        email = self.cleaned_data.get('aspi_correo')
        email_validate = Aspirante.objects.filter(aspi_correo=email).exists()
        if email_validate:
            raise forms.ValidationError('El campo no puede ser mayor a 100 caracteres')
        return email


class AspiranteCreateForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = ['aspi_primernombre', 'aspi_segundonombre', 'aspi_primerapellido',
                  'aspi_segundoapellido', 'aspi_correo', 'aspi_genero', 'tipodocumento_id',
                  'aspi_numerodocumento', 'aspi_rh', 'aspi_numerocelular', 'aspi_telefonocasa',
                  'aspi_ciudadnacimiento', 'aspi_ciudadexpediciondocumento',
                  'aspi_ciudadresidencia', 'aspi_direccion']
        labels = {
            'aspi_primernombre': 'Ingrese su primer nombre',
            'aspi_segundonombre': 'Ingrese su segundo nombre',
            'aspi_primerapellido': 'Ingrese su primer apellido',
            'aspi_segundoapellido': 'Ingrese su segundo apellido',
            'aspi_correo': 'Igrese su correo electronico',
            'aspi_genero': 'Seleccione su genero',
            'tipodocumento_id': 'Tipo de documento',
            'aspi_numerodocumento': 'Número de documento',
            'aspi_rh': 'Selecciones su RH+',
            'aspi_numerocelular': 'Ingrese su número de celular',
            'aspi_telefonocasa': 'Ingrese el número fijo de su casa',
            'aspi_ciudadnacimiento': 'Seleccione la ciudad de nacimiento',
            'aspi_ciudadexpediciondocumento': 'Seleccione la ciudad de expedicion de documento',
            'aspi_ciudadresidencia': 'Seleccione la ciudad de residencia',
            'aspi_direccion': 'Ingrese la dirección de residencia',
        }


        widgets = {
            'aspi_primernombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa primer nombre',
                    'id': 'aspi_primernombre'
                }
            ),
            'aspi_segundonombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa segundo nombre',
                    'id': 'aspi_segundonombre'
                }
            ),
            'aspi_primerapellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa primer apellido',
                    'id': 'aspi_primerapellido'
                }
            ),
            'aspi_segundoapellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa segundo apellido',
                    'id': 'aspi_segundoapellido'
                }
            ),
            'aspi_correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'Ingresa su correo electronico',
                    'id': 'aspi_correo'
                }
            ),
            'aspi_genero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione genero',
                    'id': 'aspi_genero'
                }
            ),
            'tipodocumento_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione tipo de documento',
                    'id': 'tipodocumento_id'
                }
            ),
            'aspi_numerodocumento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de documento',
                    'id': 'aspi_numerodocumento'
                }
            ),
            'aspi_rh': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su RH+',
                    'id': 'aspi_rh'
                }
            ),
            'aspi_numerocelular': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de celular',
                    'id': 'aspi_numerocelular'
                }
            ),
            'aspi_telefonocasa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número de telefono fijo',
                    'id': 'aspi_telefonocasa'
                }
            ),
            'aspi_ciudadnacimiento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione su ciudad de nacimiento',
                    'id': 'aspi_ciudadnacimiento'
                }
            ),
            'aspi_ciudadexpediciondocumento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione la ciudad de expedición de su documento',
                    'id': 'aspi_ciudadexpediciondocumento'
                }
            ),
            'aspi_ciudadresidencia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione su ciudad de residencia',
                    'id': 'aspi_ciudadresidencia'
                }
            ),
            'aspi_direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección de su residencia',
                    'id': 'aspi_direccion'
                }
            )
        }

    def clean_aspi_correo(self):
        email = self.cleaned_data.get('aspi_correo')
        email_validate = Aspirante.objects.filter(aspi_correo=email).exists()
        if email_validate:
            raise forms.ValidationError('El campo no puede ser mayor a 100 caracteres')
        return email


class InscripcionAspiranteForm(forms.ModelForm):
    idioma = forms.TextInput()