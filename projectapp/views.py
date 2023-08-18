from django.shortcuts import render,HttpResponse,redirect
from. models import registrationData
# Create your views here.


def home(req):
    return render(req, "index.html")

def login(req):
    return render(req, "login.html")

def signup(req):
    return render(req,'registration.html')

def registration(req):
    ob = registrationData()
    ob.name = req.POST.get('nm')
    ob.fname = req.POST.get('fnm')
    ob.mail = req.POST.get('email')
    ob.mob = req.POST.get('mobnum')
    ob.branch = req.POST.get('brc')
    ob.dob = req.POST.get('dob')
    ob.gender = req.POST.get('gender')
    ob.pass1 = req.POST.get('pass1')
    ob.save()
    return render(req, "login.html")

def logintask(req):
    role=req.POST.get("role")
    email=req.POST.get("email")
    password=req.POST.get("password")
    print(role)
    if (role=="Admin"):
        adm=AdminTable.objects.filter(mail=email)
        for i in adm:
            if(i.mail==email and i.pass1==password):
                return render(req, 'studentDashboard.html',{'rec':adm})

    elif (role=="Teacher"):
        return HttpResponse("Teacher Login")

    elif (role=="Student"):
        stu=registrationData.objects.filter(mail=email)
        for i in stu:
            if(i.mail==email and i.pass1==password):
                return render(req, 'studentDashboard.html',{'rec':stu})
    else:
        return redirect('/login')
    return redirect('/login')

    

