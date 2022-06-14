from django.db import models

# Create your models here.
class VaccineRegistration(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=11)
    nid = models.CharField(max_length=10, unique=True)
     
    MODERNA = 'MODERNA'
    SINOPHARM = 'SINOPHARM'
    PFIZER = 'PFIZER'
    ASTRAZENECA = 'ASTRAZENECA'
    DEFAULT = 'Not Assigned'
    
    VAC_CHOICES = [
        (MODERNA, 'MODERNA'),
        (SINOPHARM, 'SINOPHARM'),
        (PFIZER, 'PFIZER'),
        (ASTRAZENECA, 'ASTRAZENECA')
    ]
    
    VAC_CHOICES_ADMIN = [
        (MODERNA, 'MODERNA'),
        (SINOPHARM, 'SINOPHARM'),
        (PFIZER, 'PFIZER'),
        (ASTRAZENECA, 'ASTRAZENECA'),
        (DEFAULT, 'Not Assigned')
    ]
    
    p_vac = models.CharField(max_length=50, choices = VAC_CHOICES, default = SINOPHARM)
    a_vac = models.CharField(max_length=50, choices = VAC_CHOICES_ADMIN, default = DEFAULT)
    appointment = models.CharField(max_length = 60, default="Not Selected for VAC")
    vaced = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nid
    
    
class Notices(models.Model):
    news = models.TextField(max_length=255)
    
    def __str__(self):
        return self.news