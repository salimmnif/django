from django.db import models
from category.models import category
from django.core.validators import MaxValueValidator,FileExtensionValidator
from django.core.exceptions import ValidationError

from django.utils import timezone
# Create your models here.
class conference(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    start_date=models.DateField(default=timezone.now().date())
    end_date=models.DateField()
    location=models.CharField(max_length=255)
    price=models.FloatField()
    capacity=models.IntegerField(validators=[MaxValueValidator(limit_value=900,message='capacity must be under 900')])
    program=models.FileField(upload_to='files/',validators=[FileExtensionValidator(allowed_extensions=['pdf','png','jpeg','jpg'],message="c pas  faisable ya sahbi")])
    category=models.ForeignKey(category,on_delete=models.CASCADE,related_name='conference')
    
    def clean(self) :
        if self.end_date <= self.start_date:
            raise ValidationError("end date must be greater than start date")
    
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(
                    start_date=timezone.now().date(),
                    ),
             name="the start must be greater than today"

            )
        ]
