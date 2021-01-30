from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm,JobForm
from .models import Company,Job
from django.db.models import Q

# Create your views here.


def signup(request):

    # check if request is a POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # verify if the inputs are valid and also,
        # check if user already exists
        if form.is_valid():
            # retrieve user sign up details then
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('home')
    else:
        # create new instance of the UserCreationForm
        form = UserCreationForm()

    # the 3rd param in render is the data being passed down to
    # the template "signup.html"
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # get user details
            user = form.get_user()
            # log the user in
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm
    return render(request, 'registration/login.html', {'form': form})


@login_required(login_url='login')
def logged(request):
    companies = Company.objects.all()
    if request.method == 'GET':
       query = request.GET.get('q')
       if query is not None:
           results = Job.objects.filter( Q(company__company_name__icontains =query)|Q(job_name__icontains=query) | Q(description__icontains=query)).distinct()
           return render(request, 'app_templates/home.html',{'companies':companies,'jobs':results})
    companies = Company.objects.all()
    jobs = Job.objects.all()
    return render(request, 'app_templates/home.html',{'companies':companies,'jobs':jobs})

@login_required(login_url='login')
def postJob(request):
    if request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
        #get company details
            form.save()
        return redirect('home')
    else:
        form = JobForm
    return render(request, 'app_templates/postjob.html', {'form': form})

@login_required(login_url='login')
def newAccount(request):
    if request.method == 'POST':
        form = CompanyForm(data=request.POST)
        if form.is_valid():
        #get company details
            form.save()
            return redirect('home')
    else:
        form = CompanyForm
    return render(request, 'app_templates/newAccount.html', {'form': form})

@login_required(login_url='login')
def displayJob(request,jobid):
    jobdetails = Job.objects.filter(id = jobid)
    for j in jobdetails:
        jobname = j.job_name
    similarjobs = Job.objects.filter(Q(job_name__icontains=jobname)).distinct()
    return render(request,'app_templates/displayJob.html',{'jobdetails':jobdetails,'similarjobs':similarjobs})

@login_required(login_url='login')
def displayCompany(request,companyid):
    companydetails = Company.objects.filter(id=companyid)
    for c in companydetails:
        company = c.id
    companyjobs = Job.objects.filter(Q(company__id__icontains=company)).distinct()
    return render(request,'app_templates/displayCompany.html',{'companydetails':companydetails,'companyjobs':companyjobs})

def logout_view(request):
    logout(request)
    return redirect('login')