from django.forms import ModelForm
from .models import Company,Job

# Create the form class.
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'address','description']
    
class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'job_name','amount','description','requirements']