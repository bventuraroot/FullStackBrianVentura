from django.db import models


class Bookings(models.Model):
    bookings_id = models.AutoField(primary_key=True)
    courts = models.ForeignKey('Courts', models.DO_NOTHING, blank=True, null=True)
    partners = models.ForeignKey('Partners', models.DO_NOTHING, blank=True, null=True)
    frecuency = models.ForeignKey('Frecuency', models.DO_NOTHING, blank=True, null=True)
    states = models.ForeignKey('States', models.DO_NOTHING, blank=True, null=True)
    bookings_reservation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed=False
        db_table = 'bookings'
        verbose_name = "bookings"
        verbose_name_plural = "bookings"


class Courts(models.Model):
    courts_id = models.AutoField(primary_key=True)
    courts_name = models.CharField(unique=True, max_length=90)
    courts_descripcion = models.TextField(blank=True, null=True)
    courts_location = models.CharField(max_length=90, blank=True, null=True)
    courts_picture = models.CharField(max_length=190, blank=True, null=True)
    courts_state = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courts'
        verbose_name = "courts"
        verbose_name_plural = "courts"
        ordering = ['courts_id']

    def __str__(self):
        return self.courts_name


class Frecuency(models.Model):
    frecuency_id = models.AutoField(primary_key=True)
    frecuency = models.CharField(max_length=90, blank=True, null=True)
    frecuency_state = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frecuency'
        verbose_name = "frecuency"
        verbose_name_plural = "frecuency"


class Partners(models.Model):
    type_documento = (
        ('DUI', 'DUI'),
        ('PASAPORTE', 'PASAPORTE'),
        ('VISA', 'VISA')
    )

    partners_id = models.AutoField(primary_key=True)
    partners_code = models.CharField(max_length=9, blank=True, null=True)
    partners_fist_name = models.CharField(max_length=90, blank=True, null=True)
    partners_last_name = models.CharField(max_length=90, blank=True, null=True)
    partners_full_name = models.CharField(max_length=190, blank=True, null=True)
    partners_nick_name = models.CharField(max_length=90, blank=True, null=True)
    partners_nationality = models.CharField(max_length=90, blank=True, null=True)
    partners_picture = models.CharField(max_length=190, blank=True, null=True)
    partners_document_type = models.CharField(max_length=90, blank=True, null=True, choices=type_documento)
    partners_nro_document = models.CharField(max_length=10, blank=True, null=True)
    partners_address = models.CharField(max_length=190, blank=True, null=True)
    partners_phone = models.CharField(max_length=10, blank=True, null=True)
    partners_birth_date = models.DateField(blank=True, null=True)
    partners_state = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partners'
        verbose_name = "partners"
        verbose_name_plural = "partners"

    def __str__(self):
        return self.partners_full_name


class States(models.Model):
    states_id = models.AutoField(primary_key=True)
    states_name = models.CharField(max_length=90, blank=True, null=True)
    states_state = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'
        verbose_name = "states"
        verbose_name_plural = "states"

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

