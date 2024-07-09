from django.shortcuts import render, redirect
from .models import CV
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
import io
from django.contrib import messages
import os
from django.conf import settings
import base64

# Create your views here.

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
        language = request.POST.get('language')
        image = request.FILES.get('image')
        project = request.POST.get('project')
        print(name, email,phone, summary, degree, school, university, previouse_work, skills)

        cv = CV(user = request.user, name=name, email=email, phone=phone, summary=summary, degree=degree, school=school, university=university, previouse_work=previouse_work, skills=skills, language=language, image =image, project=project)
        cv.save()
        
        messages.success(request, f'Success CV created')

        return redirect('list')
    return render(request, 'pdf/accept.html')




def resume(request, id):
    user_profile = CV.objects.get(pk=id)
    user_profile.image = "http://127.0.0.1:8000"+user_profile.image.url
    print(user_profile.image)
    template = loader.get_template('pdf/resume.html')
    # return render(request, 'pdf/resume.html', {'user_profile':user_profile})
    print(id)
    html = template.render({'user_profile': user_profile})

    options = {
        'page-size': 'A4',
        'page-height': "13in",
        'page-width': "10in",
        'encoding': "UTF-8",
        'no-outline': None
    }

    path_to_wkhtmltopdf = os.path.join(settings.BASE_DIR, "wkhtmltopdf.exe")
    path_to_wkhtmltopdf = r'C:\wkhtmltox\bin\wkhtmltopdf.exe'
    

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


def editCv(request, id):
    cv = CV.objects.get(pk=id);
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
        language = request.POST.get('language')
        image = request.FILES.get('image', None)
        project = request.POST.get('project')
        print(image)
        cv.name = name
        cv.email = email
        cv.phone = phone
        cv.summary = summary
        cv.degree = degree
        cv.school = school
        cv.university = university
        cv.previouse_work = previouse_work
        cv.skills = skills
        cv.language = language 
        if image != None:
            cv.image = image
        cv.project = project
        cv.save()
        messages.success(request, f'Update Succefully')

        return redirect('list') 

    return render(request, 'pdf/edit.html', {'cv': cv})


def deleteCv(request, id):
    cv = CV.objects.get(pk=id);
    cv.delete();
    messages.success(request, f'Delete Succefully')
    return redirect('list')
