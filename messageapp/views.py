from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from messageapp.models import Msg

# Create your views here.

def testing(request):
    return HttpResponse("hello linked successfully")

def create(request):
    if request.method=='GET':
        return render(request,'create.html')
    else:
        #  fetching data from FORM
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']

        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        # return HttpResponse("data Inserted successfully")
        return redirect('/dashboard')
    
def dashboard(request):
    m=Msg.objects.all()

    context = {}
    context ['data'] = m
    return render(request,'dashboard.html',context)

def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/create')
        

def edit(request,rid):
    #print("id to be edited:",rid)
    #return HttpResponse("id to be edited:"+rid)
    if request.method=="GET":
        # m=Msg.objects.filter(id=rid)
        #print(m)
        #context={}
        #context['data']=m
        m=get_object_or_404(Msg, id=rid)
        return render(request,'edit.html',{'data':m})
    else:
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        k=Msg.objects.filter(id=rid).update(name=n,email=mail,mobile=mob,msg=msg)

        return redirect('/dashboard')