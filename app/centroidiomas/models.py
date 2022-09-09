# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.exceptions import ValidationError
from django.db import models


class Aspirante(models.Model):
    aspi_id = models.AutoField(db_column='ASPI_ID', primary_key=True)  # Field name made lowercase.
    aspi_primernombre = models.CharField(db_column='ASPI_PRIMERNOMBRE', max_length=100)  # Field name made lowercase.
    aspi_segundonombre = models.CharField(db_column='ASPI_SEGUNDONOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aspi_primerapellido = models.CharField(db_column='ASPI_PRIMERAPELLIDO', max_length=100)  # Field name made lowercase.
    aspi_segundoapellido = models.CharField(db_column='ASPI_SEGUNDOAPELLIDO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    aspi_correo = models.CharField(db_column='ASPI_CORREO', max_length=50)  # Field name made lowercase.
    aspi_genero = models.CharField(db_column='ASPI_GENERO', max_length=10)  # Field name made lowercase.
    tipodocumento_id = models.IntegerField(db_column='TIPODOCUMENTO_ID')  # Field name made lowercase.
    aspi_numerodocumento = models.CharField(db_column='ASPI_NUMERODOCUMENTO', max_length=20)  # Field name made lowercase.
    aspi_rh = models.CharField(db_column='ASPI_RH', max_length=3)  # Field name made lowercase.
    aspi_numerocelular = models.CharField(db_column='ASPI_NUMEROCELULAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aspi_telefonocasa = models.CharField(db_column='ASPI_TELEFONOCASA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aspi_estado = models.CharField(db_column='ASPI_ESTADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    aspi_ciudadnacimiento = models.IntegerField(db_column='ASPI_CIUDADNACIMIENTO')  # Field name made lowercase.
    aspi_ciudadexpediciondocumento = models.IntegerField(db_column='ASPI_CIUDADEXPEDICIONDOCUMENTO')  # Field name made lowercase.
    aspi_ciudadresidencia = models.IntegerField(db_column='ASPI_CIUDADRESIDENCIA')  # Field name made lowercase.
    aspi_direccion = models.CharField(db_column='ASPI_DIRECCION', max_length=255)  # Field name made lowercase.
    aspi_fechacambio = models.DateField(db_column='ASPI_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.

    def __str__(self):
        name = self.aspi_primernombre + self.aspi_primerapellido
        return name

    class Meta:
        managed = False
        db_table = 'ASPIRANTE'


class Convocatoriainscripcion(models.Model):
    coin_id = models.AutoField(db_column='COIN_ID', primary_key=True)  # Field name made lowercase.
    inscripcion = models.ForeignKey('Inscripcion', models.DO_NOTHING, db_column='INSCRIPCION_ID')  # Field name made lowercase.
    idioma = models.ForeignKey('Idioma', models.DO_NOTHING, db_column='IDIOMA_ID')  # Field name made lowercase.
    coin_fechainicio = models.DateField(db_column='COIN_FECHAINICIO')  # Field name made lowercase.
    coin_fechafin = models.DateField(db_column='COIN_FECHAFIN')  # Field name made lowercase.
    coin_nombre = models.CharField(db_column='COIN_NOMBRE', max_length=255)  # Field name made lowercase.
    coin_numerocupos = models.IntegerField(db_column='COIN_NUMEROCUPOS')  # Field name made lowercase.
    periodoacademico = models.ForeignKey('Periodoacademico', models.DO_NOTHING, db_column='PERIODOACADEMICO_ID')  # Field name made lowercase.
    coin_fechacambio = models.DateField(db_column='COIN_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.

    def __str__(self):
        return self.coin_nombre

    class Meta:
        managed = False
        db_table = 'CONVOCATORIAINSCRIPCION'


class Grupos(models.Model):
    grup_id = models.AutoField(db_column='GRUP_ID', primary_key=True)  # Field name made lowercase.
    grup_nombre = models.CharField(db_column='GRUP_NOMBRE', max_length=100)  # Field name made lowercase.
    grup_descripcion = models.CharField(db_column='GRUP_DESCRIPCION', max_length=255)  # Field name made lowercase.
    grup_cantidad = models.IntegerField(db_column='GRUP_CANTIDAD')  # Field name made lowercase.
    niveles = models.ForeignKey('Niveles', models.DO_NOTHING, db_column='NIVELES_ID')  # Field name made lowercase.
    grup_fechacambio = models.DateField(db_column='GRUP_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.

    def __str__(self):
        return self.grup_nombre

    class Meta:
        managed = False
        db_table = 'GRUPOS'


class Horarios(models.Model):
    hora_id = models.AutoField(db_column='HORA_ID', primary_key=True)  # Field name made lowercase.
    hora_horario = models.CharField(db_column='HORA_HORARIO', max_length=100)  # Field name made lowercase.
    salon = models.ForeignKey('Salon', models.DO_NOTHING, db_column='SALON_ID')  # Field name made lowercase.
    grupos = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='GRUPOS_ID')  # Field name made lowercase.
    hora_fechacambio = models.DateField(db_column='HORA_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.

    def __str__(self):
        return self.hora_horario

    class Meta:
        managed = False
        db_table = 'HORARIOS'


class Idioma(models.Model):
    idio_id = models.AutoField(db_column='IDIO_ID', primary_key=True)  # Field name made lowercase.
    idio_nombre = models.CharField(db_column='IDIO_NOMBRE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idio_descripcion = models.CharField(db_column='IDIO_DESCRIPCION', max_length=255)  # Field name made lowercase.
    idio_estado = models.CharField(db_column='IDIO_ESTADO', max_length=1)  # Field name made lowercase.
    idio_fechacambio = models.DateField(db_column='IDIO_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.
    niveles = models.ForeignKey('Niveles', models.DO_NOTHING, db_column='NIVELES_ID')  # Field name made lowercase.

    def __str__(self):
        return self.idio_nombre

    class Meta:
        managed = False
        db_table = 'IDIOMA'


class Inscripcion(models.Model):
    insc_id = models.AutoField(db_column='INSC_ID', primary_key=True)  # Field name made lowercase.
    insc_estadoinscripcion = models.CharField(db_column='INSC_ESTADOINSCRIPCION', max_length=255)  # Field name made lowercase.
    aspirante = models.ForeignKey(Aspirante, models.DO_NOTHING, db_column='ASPIRANTE_ID')  # Field name made lowercase.
    insc_fechainscripcion = models.DateField(db_column='INSC_FECHAINSCRIPCION')  # Field name made lowercase.
    grupos = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='GRUPOS_ID')  # Field name made lowercase.
    idioma = models.ForeignKey(Idioma, models.DO_NOTHING, db_column='IDIOMA_ID')  # Field name made lowercase.
    insc_fechacambio = models.DateField(db_column='INSC_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.

    def __str__(self):
        return self.insc_estadoinscripcion

    class Meta:
        managed = False
        db_table = 'INSCRIPCION'


class Niveles(models.Model):
    nive_id = models.AutoField(db_column='NIVE_ID', primary_key=True)  # Field name made lowercase.
    nive_nombre = models.CharField(db_column='NIVE_NOMBRE', max_length=50)  # Field name made lowercase.
    nive_numeronivel = models.CharField(db_column='NIVE_NUMERONIVEL', max_length=10)  # Field name made lowercase.
    nive_duracion = models.CharField(db_column='NIVE_DURACION', max_length=100)  # Field name made lowercase.
    nive_descripcion = models.CharField(db_column='NIVE_DESCRIPCION', max_length=255)  # Field name made lowercase.
    nive_code = models.CharField(db_column='NIVE_CODE', max_length=10)  # Field name made lowercase.
    nive_fechacambio = models.DateField(db_column='NIVE_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.

    def __str__(self):
        return self.nive_nombre

    class Meta:
        managed = False
        db_table = 'NIVELES'


class Periodoacademico(models.Model):
    peac_id = models.AutoField(db_column='PEAC_ID', primary_key=True)  # Field name made lowercase.
    peac_fechainicio = models.DateField(db_column='PEAC_FECHAINICIO')  # Field name made lowercase.
    peac_fechafin = models.DateField(db_column='PEAC_FECHAFIN')  # Field name made lowercase.
    peac_ano = models.DateField(db_column='PEAC_ANO')  # Field name made lowercase.
    peac_descripcion = models.CharField(db_column='PEAC_DESCRIPCION', max_length=255)  # Field name made lowercase.
    peac_fechacambio = models.DateField(db_column='PEAC_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.

    def __str__(self):
        return self.peac_descripcion

    class Meta:
        managed = False
        db_table = 'PERIODOACADEMICO'


class Salon(models.Model):
    salo_id = models.AutoField(db_column='SALO_ID', primary_key=True)  # Field name made lowercase.
    salo_nombre = models.CharField(db_column='SALO_NOMBRE', max_length=100)  # Field name made lowercase.
    salo_bloque = models.CharField(db_column='SALO_BLOQUE', max_length=100)  # Field name made lowercase.
    salo_fechacambio = models.DateField(db_column='SALO_FECHACAMBIO', auto_now_add=True)  # Field name made lowercase.

    def __str__(self):
        return self.salo_nombre

    class Meta:
        managed = False
        db_table = 'SALON'
