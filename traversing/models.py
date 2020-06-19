from django.db import models



# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null= True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.PositiveIntegerField(null=True)
    executive_authority = models.CharField(verbose_name = "Is This Person also has Signing Authority", max_length=15, blank=True, null=True)
    exec_first_name = models.CharField("Executive First Name", max_length=30, blank=True, null=True)
    exec_last_name = models.CharField("Executive Last Name", max_length=30, blank=True, null=True)
    exec_title = models.CharField("Executive Title/Position", max_length=1024, blank=True, null=True)
    exec_email = models.EmailField("Executive - Email", max_length=254, blank=True, null=True)
    exec_phone_number = models.CharField("Executive Phone Number", max_length=17, blank=True, null=True)
    payment_type = models.CharField(max_length=30)
    institution_code = models.CharField(max_length=30)
    branch_number = models.CharField(max_length=30)
    account_number = models.CharField(max_length=30)
