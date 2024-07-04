from django.shortcuts import render, redirect
from .models import CV
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
import io
from django.contrib import messages

# Create your views here.
path_to_wkhtmltopdf = r'C:\wkhtmltox\bin\wkhtmltopdf.exe'

@login_required
def accept(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        summary = request.POST.get('summary')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        previouse_work = request.POST.get('previouse_work')
        skills = request.POST.get('skills')
        print(name, email,phone, summary, degree, school, university, previouse_work, skills)

        cv = CV(user = request.user, name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previouse_work=previouse_work, skills=skills)
        cv.save()
    return render(request, 'pdf/accept.html')


def resume(request, id):
    print(id)
    user_profile = CV.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }


    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    pdf = pdfkit.from_string(html, False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'


    # Redirect to another page
    return response

@login_required
def list(request):
    profile = CV.objects.filter(user=request.user)
    return render(request, 'pdf/list.html', {'profiles':profile})