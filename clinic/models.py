from django.db import models

class Appointment(models.Model):
	# just dummy docs names
	VIKTOROVA = 'Viktorova'
	IVANOVA = 'Ivanova'
	DOCS_NAMES = (
		(VIKTOROVA, 'Viktorova'),
		(IVANOVA, 'Ivanova'),
    )
	doc_name = models.CharField(max_length=2,
                                choices=DOCS_NAMES,
                                default=VIKTOROVA)
	visit_date = models.DateField('date of the visit')
	visit_time = models.TimeField('time of the visit')
	client_name = models.CharField(max_length=200)

# Create your models here.
