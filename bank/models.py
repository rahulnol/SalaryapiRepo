from django.db import models

# Create your models here.
class BankDetail(models.Model):
    ACCOUNT_TYPES = (
        ('saving', 'Saving Account'),
        ('current', 'Current Account'),
        ('salary', 'Salary Account'),
    )
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    account_number = models.PositiveIntegerField(blank=True, null=True)
    ifsc_code = models.CharField(max_length=25)
    branch_name = models.CharField(max_length=25)
    account_type = models.CharField(choices=ACCOUNT_TYPES, default='salary',max_length=25)

