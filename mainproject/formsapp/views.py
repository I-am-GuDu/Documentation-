from django.shortcuts import render
from django.http import HttpResponse
from .models import Submission

def submit_view(request):
    if request.method == 'POST':
        hobbies_list = request.POST.getlist('Hobbies')
        hobbies = ', '.join(hobbies_list)

        sub = Submission(
            name=request.POST.get('name',''),
            address=request.POST.get('address',''),
            gender=request.POST.get('gender',''),
            dob=request.POST.get('dob') or None,
            phone=request.POST.get('phone',''),
            age=(int(request.POST['age']) if request.POST.get('age') else None),
            email=request.POST.get('email',''),
            password=request.POST.get('password',''),
            image=request.FILES.get('image'),
            aadhaar=request.FILES.get('addhar') or request.FILES.get('aadhaar'),
            tenth=request.FILES.get('10th') or request.FILES.get('tenth'),
            country=request.POST.get('country',''),
            hobbies=hobbies,
            color=request.POST.get('color',''),
        )
        sub.save()
        return HttpResponse("Submitted successfully.")
    return render(request, 'index.html')
