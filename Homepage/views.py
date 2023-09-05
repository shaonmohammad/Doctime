from django.shortcuts import render, redirect
from Patients.models import Patient
from .forms import PatientForm


def homepage(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'homepage/homepage.html', context)


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('homepage')
    else:
        form = PatientForm()
    return render(request, 'homepage/add_patients.html', {'patients': form})


def searching(request):
    name = request.POST.get('SearchPatient')
    if name:
        patients = Patient.objects.filter(name__icontains=name)
    else:
        patients = Patient.objects.all()

    return render(request, 'homepage/search.html', {'patients': patients})


# def search(request):
#     title = request.POST.get('SearchPatient')

#     if title:
#         books = BookList.objects.filter(title__icontains=title)
#     else:
#         books = BookList.objects.all()

#     return render(request, 'BookShelf/search-result.html', {'books':books, 'query':title})
