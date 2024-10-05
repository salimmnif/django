from django.db import models
from django.contrib.auth.models import AbstractUser
from conference.models import conference
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
def email_validate(value):
    if not value.endswith('@esprit.tn'):
        raise ValidationError('email invalid')
class participants(AbstractUser):
    cin_validator=RegexValidator(regex=r'^{8}$')
    cin=models.CharField(primary_key=True,max_length=8)
    email=models.EmailField(unique=True,max_length=255,validators=[email_validate])
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(max_length=255,unique=True)
    USENAME_FIELD='usename'
    CHOICES=(
        ('etudiant','etudiant'),
        ('chercheur','chercheur'),
        ('docteur','docteur'),
        ('enseignant','enseignant')
    )

    participants_category=models.CharField(max_length=255,choices=CHOICES)
    reservations=models.ManyToManyField(conference,through='Reservation',related_name='Reservation')


class Reservation(models.Model):
    conference=models.ForeignKey(conference,on_delete=models.CASCADE)
    participants=models.ForeignKey(participants,on_delete=models.CASCADE)
    comfirmed=models.BooleanField(default=False)
    reservation_date=models.DateField(auto_now_add=True)
    def clean(self) :
        if self.conference.start_date < timezone.now().date():
            raise ValidationError("you can only reserve for upgoing days")
        Reservation_count=Reservation.objects.filter(participants=self.participants,
                                                     Reservation_date=self.reservation_date)
        if Reservation_count>=3:
            raise ValidationError("you can only make upto 3 reservations")
    class meta:
        uique_together=('participants','conference')