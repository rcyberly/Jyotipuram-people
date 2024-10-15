from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from Community.models import Community
from Jpeople.models import Jpeople
from django.core.paginator import Paginator
from django.http import Http404
def jphomepage(request):
    j = ''
    if request.method == ('POST'):
        yourtext = request.POST.get('yourtext')
        fileup = request.POST.get('fileup')
        fdata = Jpeople(yourtext=yourtext,fileup=fileup)
        fdata.save()
        j = "your data is saved"
    filedata = Jpeople.objects.all()
    filedatabase = {
        'filedata': filedata,
        'j':j,
        }

    return render(request,"jphomepage.html",filedatabase)

def benefits(request):
    return render(request,"benefits.html")

def clubmandir1(request):
    return render(request,"clubmandir1.html")

def clubmandir2(request):
    return render(request,"clubmandir2.html")

def lopage(request):
    communify = Community.objects.all()
    communify = {
        'communify':communify,
        } 
    return render(request,"lopage.html",communify)
    

def community(request):
    t = ''
    if request.method == ('POST'):
        file = request.POST.get('file')
        name = request.POST.get('name')
        qtype = request.POST.get('qtype')
        qnumber = request.POST.get('qnumber')
        school = request.POST.get('school')
        statename = request.POST.get('statename')
        phonenumber = request.POST.get('phonenumber')
        commun = Community(file=file,name=name,qtype=qtype,qnumber=qnumber,school=school,statename=statename,phonenumber=phonenumber)
        commun.save()
        t = ("your data has been saved")  
        commun = Community.objects.all()
    return render(request,"community.html",{'t':t})

def dbbsb(request):
    return render(request,"dbbsb.html")

def ddd(request):
    return render(request,"ddd.html")

def derababa(request):
    return render(request,"derababa.html")

def durgamandir1(request):
    return render(request,"durgamandir1.html")

def durgamandir2(request):
    return render(request,"durgamandir2.html")

def gurudwara(request):
    return render(request,"gurudwara.html")

def gurudwarasahib(request):
    return render(request,"gurudwarasahib.html")

def gurudwarasahibjyotipuram(request):
    return render(request,"gurudwarasahibjyotipuram.html")

def home(request):
    return render(request,"home.html")

def kalkajireasi(request):
    return render(request,"kalkajireasi.html")

def lnt1(request):
    return render(request,"lnt1.html")

def lnt2(request):
    return render(request,"lnt2.html")

def places(request):
    return render(request,"places.html")

def siyadbaba(request):
    return render(request,"siyadbaba.html")

def swargashram(request):
    return render(request,"swargashram.html")

def swargashrumtwo(request):
    return render(request,"swargashrumtwo.html")

def talwaracoloney(request):
    return render(request,"talwaracoloney.html")

def untitled1(request):
    return render(request,"untitled1.html")