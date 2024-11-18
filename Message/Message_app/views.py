from django.shortcuts import render,HttpResponse,redirect
from .models import stud
# Create your views here.
def create(request):
    if request.method=='POST':
          n=request.POST['uname']
          mail=request.POST['uemail']
          mob=request.POST['mobile']
          msg=request.POST['msg']

          m=stud.objects.create(name=n,email=mail,mobile=mob,msg=msg)
          m.save()
          return redirect('/dashboard')
    
    else:  
 
     print("request is :",request.method)
     return render(request,'create.html')
def dashboard(request):
      m=stud.objects.all()
      context={}
      context['data']=m   
      return render(request,'dashboard.html',context)   
def edit(request,rid):
      if request.method=='GET':
        m=stud.objects.get(id=rid)      
        context={}
        context['data']=m
        return render(request,'edit.html',context)
      else:
          upname=request.POST['uname']
          upmail=request.POST['uemail']
          upmob=request.POST['mobile']
          upmsg=request.POST['msg']
          m=stud.objects.filter(id=rid)
          #update stud set name=?,email=?,mob=?,msg=? where id=rid
          m.update(name=upname,email=upmail,mobile=upmob,msg=upmsg)
          return redirect('/dashboard')
def delete(request,rid):
      m=stud.objects.filter(id=rid) #
      m.delete()
      #delete from  stud where id=?
      return redirect('/dashboard')          