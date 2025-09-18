from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import usersForm
from services.models import Services
from news.models import News



def homepage(request):
    newsData=News.objects.all()
    servicesData=Services.objects().all().order_by('-services_title')[:3]
    
    # for a in servicesData:
    #     print(a.services_icon)
    # print(services)    
    data={
        'servicesData':servicesData,
        'newsData':newsData
    }
    return render(request,"index.html",data)

def newsDetails(request,slug):

    newsDetails=News.objects.get(news_slug=slug)
    
    data={
        'newsDetails':newsDetails
    }
    return render(request,'newsdetails.html',data)



def index(request):
    return render(request, 'index.html')

def services(request):
    ServiceData = Services.objects.all()
    if request.method == 'GET':
        st = request.GET.get('servicename')   # ✅ sahi
        if st is not None:
            ServiceData = Services.objects.filter(services_title=st)  # ✅ st use karo, str nahi
    data = {
        'servicesData': ServiceData
    }
    return render(request, 'services.html', data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def submitform(request):
    try:
        
        if request.method=='POST':
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            n3=int(request.POST.get('num3'))
            return HttpResponse(request)
            finalans=n1+n2+n3
            data={
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'output':finalans
                
            }
            return HttpResponse(finalans)
    except:
        pass
            




# def userForm(request):
#     finalans=0
#     try:
#         n1=int(request.Get['num1'])
#         n2=int(request.Get['num2'])
#         n3=int(request.Get['num3'])
#         print(n1+n2+n3)
#         finalans=n1+n2+n3
#     except:
#            pass
   
    
#     return render(request,'userForm.html',{'output':finalans})

# def userForm(request):
#     finalans = 0
#     try:
#         n1 = int(request.GET.get('num1', 0))
#         n2 = int(request.GET.get('num2', 0))
#         n3 = int(request.GET.get('num3', 0))
#         print(n1 + n2 + n3)
#         finalans = n1 + n2 + n3
#     except Exception as e:
#         print("Error:", e)
    
                               # post method
def userForm(request):
    finalans = 0
    fn = usersForm()   # ✅ form ka object

    data = {'form': fn}

    try:
        if request.method == 'POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            finalans = n1 + n2 + n3

            data = {
                'form': fn,
                'output': finalans
            }

            url = '/contact/?output={}'.format(finalans)
            return redirect(url)

    except Exception as e:
        print("error:", e)

    return render(request, 'userForm.html', data)
            
            
    
                              
    
    
    
    return render(request, 'userForm.html', {'output': data})