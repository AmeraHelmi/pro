import os, sys
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *
from django.db.models import Sum
from datetime import datetime
from datetime import date , time
from django.http import JsonResponse
import datetime
import json
from django.template.loader import get_template
from django.template import Context
import cStringIO as StringIO
from cgi import escape
####################################################################
# start method for system
def start(request):
    if request.session.get("email"):
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        return  render(request,'index.html',{'username':username,'role':role})
    else:
        return render(request,'index.html')
#####################################################################
# to print pdf 
def pdf_printer(request):
    # print pdf  
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, request.session.get("username"))
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
####################################################################
# search by date in "elyomia page"
def search(request):
    if request.method == 'POST':
        item_date=request.POST.get("datepicker")
        if item_date:
            month,day,year = item_date.split('/')
            month=month.encode('utf-8')
            day=day.encode('utf-8')
            year=year.encode('utf-8')
            print("day: ",day," month: ",month," year: ",year)
            day=int(day)
            month=int(month)
            year=int(year)
            testdate=datetime.datetime(year,month,day)
            ss_items=Item.objects.all().values_list('item_title',flat=True)
            items=Item.objects.filter(item_date=testdate)
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            if request.session.get("project"):
                project=request.session.get("project")
                pro_obj=Project.objects.get(name=project)
                today_date=date.today()
            # items=Item.objects.filter(item_date=today_date,project=pro_obj)
                all_price=0
                for item in items:
                    ss=int(item.item_total.encode('utf-8'))
                    all_price=all_price+ss
                return render(request,'today.html',{'today_date':today_date,'username':username,'role':role,'items':items,'test_date':testdate,'all_items':ss_items,'all_price':all_price,'project':project})
            else:
                return render(request,'today.html',{'username':username,'role':role})
        else:
            today_date=date.today()
            ss_items=Item.objects.all().values_list('item_title',flat=True)
            items=Item.objects.filter(item_date=today_date)
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            if request.session.get("project"):
                project=request.session.get("project")
                pro_obj=Project.objects.get(name=project)            
                items=Item.objects.filter(item_date=today_date,project=pro_obj)
                all_price=0
                for item in items:
                    ss=int(item.item_total.encode('utf-8'))
                    all_price=all_price+ss
                return render(request,'today.html',{'project':project,'username':username,'role':role,'items':items,'today_date':today_date,'all_items':ss_items,'all_price':all_price})
            else:
                return render(request,'today.html',{'username':username,'role':role,'today_date':today_date})

#####################################################################
def projects(request):
    if request.session.get("email"):
        projects=Project.objects.all()
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        return render(request,'projects.html',{'username':username,'role':role,'projects':projects})
    else:
        return render(request,'projects.html')
####################################################################
# index method for "elyomia page"
def today(request):
    today_date=date.today()
    ss_items=Item.objects.all().values_list('item_title',flat=True)
    items=Item.objects.filter(item_date=today_date)
    if request.session.get("email"):
        if request.session.get("project"):
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
            items=Item.objects.filter(item_date=today_date,project=pro_obj)
            all_price=0
            for item in items:
                ss=int(item.item_total.encode('utf-8'))
                all_price=all_price+ss
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            project=request.session.get("project")
            return render(request,'today.html',{'project':project,'username':username,'role':role,'items':items,'today_date':today_date,'all_items':ss_items,'all_price':all_price})
        else:
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            
            return render(request,'today.html',{'username':username,'role':role,'today_date':today_date})
    else:

        return render(request,'today.html')
########################################################################
# test for date range in search process
def test(request):
    persons=Item.objects.filter(item_date__range=["2011-01-01", "2015-12-01"])
    email=request.session.get("email")
    user_obj=User.objects.get(user_email=email)
    request.session['username']=user_obj.user_name
    username=request.session.get("username")
    request.session['role']=user_obj.user_role
    role=request.session.get("role")
    return render(request,'test.html',{'username':username,'role':role,'persons':persons}) 
#######################################################################
# index method for ma2wlen page
def m2alen(request):
    if request.session.get("email"):
        if request.session.get("project"):
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
            persons=M2awel.objects.filter(project=pro_obj)
            objs = Transaction.objects.values('m2awel').annotate(data_sum=Sum('action_paid'))
            for obj in objs:
                for key,value in obj.iteritems():
                    if key == "m2awel":
                        m_obj=M2awel.objects.get(id=obj['m2awel'])
                        m_obj.paid=obj['data_sum']
                        m_obj.save()
        # persons=M2awel.objects.all()
            users=M2awel.objects.all()
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
        # project=request.session.get("project")
            today_date=date.today()
            return render(request,'m2alen.html',{'today_date':today_date,'project':project,'username':username,'role':role,'persons':persons,'objs':objs,'users':users}) 
        else:
            return render(request,'m2alen.html')
    else:
      
        return render(request,'m2alen.html')
#######################################################################
def getproinfo(request):
    if request.method == 'POST':
        job = request.POST.get('jobs', None)  
        pro_obj=Project.objects.get(name=job)
        username=request.session.get("username")
        role=request.session.get("role")
        items=Item.objects.filter(project=pro_obj)
        m2awelen=M2awel.objects.filter(project=pro_obj)
        shekat=Shek.objects.filter(project=pro_obj)
        return render(request,'proinfo.html',{'username':username,'role':role,'items':items,'m2awelen':m2awelen,'shekat':shekat})
#######################################################################
# to make report 
def accountsbydate(request):
    if request.method == 'POST':
        date1=request.POST.get("datepicker1")
        date2=request.POST.get("datepicker2")
        if date1 and date2 :
            month1,day1,year1 = date1.split('/')
            month1=month1.encode('utf-8')
            day1=day1.encode('utf-8')
            year1=year1.encode('utf-8')
            day1=int(day1)
            month1=int(month1)
            year1=int(year1)
            # date1=date(year1,month1,day1)
            # date1=datetime.datetime(year1,month1,day1)
            month2,day2,year2 = date2.split('/')
            month2=month2.encode('utf-8')
            day2=day2.encode('utf-8')
            year2=year2.encode('utf-8')
            
            day2=int(day2)
            month2=int(month2)
            year2=int(year2)
            # start = date(year1, month1, day1)
            # end = date(year2, month2, day2)

            start=datetime.datetime(year1,month1,day1)
            end=datetime.datetime(year2,month2,day2)
      
            # d.strptime("%Y-%m-%d")
            # start=str(start)
            # end=str(end)
            # start=datetime.datetime.strptime(start, "%Y-%m-%d")
            # end=datetime.datetime.strptime(end, "%Y-%m-%d")
            # start=start.strptime("%Y-%m-%d")
            # end=end.strptime("%Y-%m-%d")
            # date2=date(year2,month2,day2)
            # date2=datetime.datetime(year2,month2,day2)
            # ss_items=Item.objects.all().values_list('item_title',flat=True)
            if request.session.get("project"):
                project=request.session.get("project")
                pro_obj=Project.objects.get(name=project)
           
            # items=Item.objects.filter(item_date__gt=datetime.date(year1,month1, day1),item_date__lt=datetime.date(year2, month2, day2))
                items=Item.objects.filter(item_date__range=[start, end],project=pro_obj)
                actions=Transaction.objects.filter(action_date__range=[date1,date2])
                email=request.session.get("email")
                user_obj=User.objects.get(user_email=email)
                request.session['username']=user_obj.user_name
                username=request.session.get("username")
                request.session['role']=user_obj.user_role
                role=request.session.get("role")
                request.session["date1"]=date1
                request.session["date2"]=date2
                today_date=date.today()
                dd_items=Item.objects.filter(item_date=today_date,project=pro_obj)
                all_price=0
                for item in dd_items:
                    ss=int(item.item_total.encode('utf-8'))
                    all_price=all_price+ss
                dd_actions=Transaction.objects.filter(action_date=today_date)
                for action in dd_actions:
                    dd=int(action.action_paid)
                    all_price=all_price+dd
                return render(request,'accounts.html',{'project':project,'all_price':all_price,'username':username,'role':role,'items':items,'actions':actions})
            else:
                return render(request,'accounts.html',{'username':username,'role':role})
#######################################################################
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
#######################################################################
def report(request):
    today_date=date.today()
    ss_items=Item.objects.all().values_list('item_title',flat=True)
    items=Item.objects.filter(item_date=today_date)
    all_price=0
    for item in items:
        ss=int(item.item_total.encode('utf-8'))
        all_price=all_price+ss
    ss_actions=Transaction.objects.filter(action_date=today_date)
    for action in ss_actions:
        dd=int(action.action_paid)
        all_price=all_price+dd
    # results['today_date']=today_date
    # results['all_price']=all_price
    return render_to_pdf(
            'mytemplate.html',
            {
                'pagesize':'A4',
                'today_date': today_date,
                'all_price':all_price,
            }
        )
        # print pdf with today date and all_price
#######################################################################
# to search of m2awel
def m2awelsearch(request):
    today_date=date.today()
    if request.method == 'POST':
        name = request.POST.get('names', None)  
        job=request.POST.get('jobs',None)
        name=name.encode('utf-8') 
        if request.session.get("project"):
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
            print("name: ",name)
            if name != 'defult' and job != 'defult':
                users=M2awel.objects.all()
                try:
                    obj=M2awel.objects.get(name=name,job=job)
               
                except M2awel.DoesNotExist:
                    obj=None
                email=request.session.get("email")
                user_obj=User.objects.get(user_email=email)
                request.session['username']=user_obj.user_name
                username=request.session.get("username")
                request.session['role']=user_obj.user_role
                role=request.session.get("role")
                return render(request,'getm2awel.html',{'today_date':today_date,'project':project,'username':username,'role':role,'obj':obj,'users':users})
            elif name == 'defult' and job == 'defult':
                persons=M2awel.objects.all()
                users=M2awel.objects.all()
                email=request.session.get("email")
                user_obj=User.objects.get(user_email=email)
                request.session['username']=user_obj.user_name
                username=request.session.get("username")
                request.session['role']=user_obj.user_role
                role=request.session.get("role")
                return render(request,'m2alen.html',{'today_date':today_date,'project':project,'username':username,'role':role,'persons':persons,'users':users}) 
            elif name == 'defult' and job != 'defult':
                persons=M2awel.objects.filter(job=job)
                users=M2awel.objects.all()
                email=request.session.get("email")
                user_obj=User.objects.get(user_email=email)
                request.session['username']=user_obj.user_name
                username=request.session.get("username")
                request.session['role']=user_obj.user_role
                role=request.session.get("role")
                return render(request,'m2alen.html',{'today_date':today_date,'project':project,'username':username,'role':role,'persons':persons,'users':users}) 
            elif name != 'defult' and job == 'defult':
                persons= M2awel.objects.filter(name=name)
                users=M2awel.objects.all()
                email=request.session.get("email")
                user_obj=User.objects.get(user_email=email)
                request.session['username']=user_obj.user_name
                username=request.session.get("username")
                request.session['role']=user_obj.user_role
                role=request.session.get("role")
                return render(request,'m2alen.html',{'today_date':today_date,'project':project,'username':username,'role':role,'persons':persons,'users':users})            
        else:
            username=request.session.get("username")
            role=request.session.get("role")
            users=M2awel.objects.all()
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            today_date=date.today()
            return render(request,'m2alen.html',{'today_date':today_date,'username':username,'role':role,'users':users})    
#######################################################################
# index method for "shekat page"
def shekat(request):
    if request.session.get("email"):
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        today_date=date.today()
        if request.session.get("project"):
            today_date=date.today()
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
            items=Shek.objects.filter(project=pro_obj,date=today_date)
            return render(request,'shekat.html',{'project':project,'items':items,'role':role,'username':username,'today_date':today_date})
        else:
            return render(request,'shekat.html')
    else:
       
        # items=Shek.objects.filter(project=pro_obj,date=today_date)
        return render(request,'shekat.html')
#######################################################################
# index page for "accounts page"
def accounts(request):
    if request.session.get("email"):
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        today_date=date.today() 
        if request.session.get("project"):
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
       
            dd_items=Item.objects.filter(item_date=today_date,project=pro_obj)
            all_price=0
            for item in dd_items:
                ss=int(item.item_total.encode('utf-8'))
                all_price=all_price+ss
            dd_actions=Transaction.objects.filter(action_date=today_date)
            for action in dd_actions:
                dd=int(action.action_paid)
                all_price=all_price+dd
            all_projects=Project.objects.all()
            return render(request,'accounts.html',{'project':project,'all_price':all_price,'username':username,'role':role,'all_projects':all_projects})
        else:
            return render(request,'accounts.html',{'username':username,'role':role})
    else:
        username=request.session.get("username")
        role=request.session.get("role")
        all_projects=Project.objects.all()
        return render(request,'accounts.html',{'all_projects':all_projects,'username':username,'role':role})
#######################################################################
# registeration method
def register(request):
    # registeration form
    if request.method == 'POST':
        # get information of user
        
        u_name=request.POST.get("name")
        u_email=request.POST.get("email")
        u_pass=request.POST.get("pass")
        if request.POST.get("age"):
            u_age=request.POST.get("age")
            u_obj=User(user_name=u_name,user_email=u_email,user_password=u_pass,user_age=u_age)
            u_obj.save()
            request.session["email"]=u_obj.user_email
            email=request.session.get("email")
            request.session['username']=u_obj.user_name
            username=request.session.get("username")
            request.session['role']=u_obj.user_role
            role=request.session.get("role")
            return render(request,'index.html',{'username':username,'role':role})
        else:
            u_obj=User(user_name=u_name,user_email=u_email,user_password=u_pass)
            u_obj.save()
            request.session['email']=u_obj.user_email
            email=request.session.get("email")
            request.session['username']=u_obj.user_name
            username=request.session.get("username")
            request.session['role']=u_obj.user_role
            role=request.session.get("role")
            return render(request,'index.html',{'username':username,'role':role})
    else:
        return render(request,'reg.html')
##########################################################################
# login method
def login(request):
    # login form
    if request.method == 'POST':
        # get information of user
        u_email=request.POST.get("email")
        u_pass=request.POST.get("pass")
        if User.objects.filter(user_email=u_email,user_password=u_pass).exists():
            obj=User.objects.get(user_email=u_email,user_password=u_pass)
            request.session["username"]=obj.user_name
            request.session["role"]=obj.user_role
            request.session["email"]=obj.user_email
            return render(request,'index.html',{'username':obj.user_name,'role':obj.user_role})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
####################################################################################
# logout method
def logout(request):
    del request.session["username"]
    del request.session["role"]
    del request.session["email"]
    # request.session['project']="os"
    # del request.session["project"]
    return render(request,'index.html')
###################################################################################
# to add new item in Item table
def additem(request):
    if request.method == 'POST':
        # get information of item
        i_title=request.POST.get("title")
        if request.POST.get("price"):
            i_price=request.POST.get("price")
        else:
            i_price=""
        if request.POST.get("amount"):
            i_amount=request.POST.get("amount")
        else:
            i_amount=""
        if request.POST.get("total"):
            i_total=request.POST.get("total")
        else:
            i_total=str(int(i_amount) * int(i_price))
        if request.POST.get("notes"):
            i_notes=request.POST.get("notes")
        else:
            i_notes=""
        project = request.POST.get('projects', None) 
        if project != 'defult':
            pro_obj=Project.objects.get(name=project)
            obj=Item(project=pro_obj,item_title=i_title,item_price=i_price,item_amount=i_amount,item_total=i_total,item_date=date.today(),item_description=i_notes)
            if Item.objects.filter(project=pro_obj,item_title=i_title,item_price=i_price,item_amount=i_amount,item_total=i_total,item_date=date.today(),item_description=i_notes).exists():
                # return items page
                request.session['project']=project
            else:
                obj.save()
                request.session['project']=project
        else:
            if request.session.get("project"):
                project=request.session.get("project")
                pro_obj=Project.objects.get(name=project)
            
                obj=Item(project=pro_obj,item_title=i_title,item_price=i_price,item_amount=i_amount,item_total=i_total,item_date=date.today(),item_description=i_notes)
            if Item.objects.filter(project=pro_obj,item_title=i_title,item_price=i_price,item_amount=i_amount,item_total=i_total,item_date=date.today(),item_description=i_notes).exists():
                # return items page
                request.session['project']=project
            else:
                obj.save()
                request.session['project']=project
        today_date=date.today()
        ss_items=Item.objects.all().values_list('item_title',flat=True)
        pro_obj=Project.objects.get(name=project)
        items=Item.objects.filter(item_date=today_date,project=pro_obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        if request.session.get("project"):
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
   
            items=Item.objects.filter(item_date=today_date,project=pro_obj)
            all_price=0
            for item in items:
                ss=int(item.item_total.encode('utf-8'))
                all_price=all_price+ss
            return render(request,'today.html',{'project':project,'username':username,'role':role,'items':items,'today_date':today_date,'all_items':ss_items,'all_price':all_price})
    else:
        today_date=date.today()
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        projects=Project.objects.all()
        if request.session.get("project"):
            project=request.session.get("project")
            return render(request,'additem.html',{'project':project,'projects':projects,'username':username,'role':role,'today_date':today_date})
#############################################################################
def addpro(request):
    if request.method == 'POST':
        pro_name=request.POST.get("name")
        obj=Project(name=pro_name)
        obj.save()
        request.session["project"]=pro_name
        today_date=date.today()
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        projects=Project.objects.all()
        request.session['status']="addpro"
        today_date=date.today()
        project=request.session.get("project")
        return render(request,'additem.html',{'project':project,'projects':projects,'username':username,'role':role,'today_date':today_date})        
    else:
        today_date=date.today()
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role 
        if request.session.get("project"):
            project=request.session.get("project")
    
            role=request.session.get("role")
            return render(request,'addpro.html',{'project':project,'username':username,'role':role,'today_date':today_date})
        return render(request,'addpro.html',{'username':username,'role':role,'today_date':today_date})
##########################################################################
def addproj(request):
    if request.method == 'POST':
        pro_name=request.POST.get("name")
        if Project.objects.filter(name=pro_name).exists():
            request.session["project"]=pro_name
      
            today_date=date.today()
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
            items=Item.objects.filter(item_date=today_date,project=pro_obj)
            # items=Item.objects.filter(item_date=today_date)
            all_price=0
            for item in items:
                ss=int(item.item_total.encode('utf-8'))
                all_price=all_price+ss
            projects=Project.objects.all()
            return render(request,'projects.html',{'projects':projects,'username':username,'role':role})                   
        else:
            obj=Project(name=pro_name)
            obj.save()
            request.session["project"]=pro_name
           
            today_date=date.today()
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
            items=Item.objects.filter(item_date=today_date,project=pro_obj)
            all_price=0
            for item in items:
                ss=int(item.item_total.encode('utf-8'))
                all_price=all_price+ss
            projects=Project.objects.all()
            return render(request,'projects.html',{'projects':projects,'username':username,'role':role})       
    else:
        today_date=date.today()
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        if request.session.get("project"):
            project=request.session.get("project")
 
            return render(request,'addproj.html',{'project':project,'username':username,'role':role,'today_date':today_date})
        return render(request,'addproj.html',{'username':username,'role':role,'today_date':today_date})	
###################################################################
def editpro(request,pid):
    pro_obj=Project.objects.get(id=pid)
    if request.method == 'POST':
        if request.POST.get("name"):
            pro_obj.name=request.POST.get("name")
            pro_obj.save()
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            projects=Project.objects.all()
            return render(request,'projects.html',{'username':username,'role':role,'projects':projects})
        else:
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            projects=Project.objects.all()
            return render(request,'projects.html',{'username':username,'role':role,'projects':projects})
    else:
        return render(request,'editpro.html',{'pro_name':pro_obj.name,'pro_id':pro_obj.id})
####################################################################
def delipro(request,pid):
    pro_obj=Project.objects.get(id=pid)
    Project.objects.filter(id=pid).delete()
    email=request.session.get("email")
    user_obj=User.objects.get(user_email=email)
    request.session['username']=user_obj.user_name
    username=request.session.get("username")
    request.session['role']=user_obj.user_role
    role=request.session.get("role")
    projects=Project.objects.all()
    if request.session.get("project") == pro_obj.name :
        del request.session['project']
    return render(request,'projects.html',{'username':username,'role':role,'projects':projects})
####################################################################
def usepro(request,pid):
    pro_obj=Project.objects.get(id=pid)
    request.session['project']=pro_obj.name
    project=request.session.get("project")
    items=Item.objects.filter(project=pro_obj)
    all_price=0
    for item in items:
        ss=int(item.item_total.encode('utf-8'))
        all_price=all_price+ss
    email=request.session.get("email")
    user_obj=User.objects.get(user_email=email)
    request.session['username']=user_obj.user_name
    username=request.session.get("username")
    request.session['role']=user_obj.user_role
    role=request.session.get("role")
    today_date=date.today()
    return render(request,'today.html',{'project':project,'username':username,'role':role,'items':items,'all_price':all_price})
####################################################################
# to add new shek 
def addshek(request):
    if request.method == 'POST':
        # get information of shek
        i_num=request.POST.get("num")
        # i_date=request.POST.get("date
        i_date=date.today()
        i_amount=request.POST.get("amount") 
        # if request.session.get("project"):
        project=request.session.get("project")
        pro_obj=Project.objects.get(name=project)

        obj=Shek(num=i_num,date=i_date,amount=i_amount,project=pro_obj)
        if Shek.objects.filter(num=i_num,date=i_date,amount=i_amount,project=pro_obj).exists():
            items=Shek.objects.filter(project=pro_obj)
        else:

            obj.save()
        items=Shek.objects.filter(project=pro_obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        today_date=date.today()
        return render(request,'shekat.html',{'today_date':today_date,'project':project,'username':username,'items':items,'role':role})
    else:
        today_date=date.today()
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        # if request.session.get("project"):
        project=request.session.get("project")
        
        return render(request,'addshek.html',{'today_date':today_date,'project':project,'username':username,'role':role})
#############################################################################
# to add new m2awel
def addm2awel(request):
    if request.method == 'POST':
        # get information of m2awel
        i_name=request.POST.get("name")
        i_money=request.POST.get("money")
        i_paid=request.POST.get("paid")
        i_job=request.POST.get("job")
        # if request.session.get("project"):
        project=request.session.get("project")
        pro_obj=Project.objects.get(name=project)

        obj=M2awel(name=i_name,money=i_money,paid=i_paid,job=i_job,project=pro_obj)
        if M2awel.objects.filter(name=i_name,money=i_money,paid=i_paid,job=i_job,project=pro_obj).exists():
            persons=M2awel.objects.filter(project=pro_obj)   
        else:
            obj.save()
        persons=M2awel.objects.filter(project=pro_obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        return render(request,'m2alen.html',{'project':project,'username':username,'persons':persons,'role':role})
    else:
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        # if request.session.get("project"):
        project=request.session.get("project")
        
        return render(request,'addm2awel.html',{'project':project,'username':username,'role':role})
#############################################################################
# to delete existing item 
def delitem(request,uid):
    Item.objects.filter(id=uid).delete()
    today_date=date.today()
    # if request.session.get("project"):
    project=request.session.get("project")
    pro_obj=Project.objects.get(name=project)

    ss_items=Item.objects.all().values_list('item_title',flat=True)
    items=Item.objects.filter(item_date=today_date)
    email=request.session.get("email")
    user_obj=User.objects.get(user_email=email)
    request.session['username']=user_obj.user_name
    username=request.session.get("username")
    request.session['role']=user_obj.user_role
    # project=request.session.get("project")
    # pro_obj=Project.objects.get(name=project)
    # items=Item.objects.filter(item_date=today_date,project=pro_obj)
    all_price=0
    for item in items:
        ss=int(item.item_total.encode('utf-8'))
        all_price=all_price+ss
    role=request.session.get("role")
    return render(request,'today.html',{'project':project,'username':username,'items':items,'today_date':today_date,'all_items':ss_items,'all_price':all_price,'role':role})

##############################################################################
# to delete existing shek
def delshek(request,uid):
    Shek.objects.filter(id=uid).delete()
    today_date=time.strftime("%d/%m/%Y")
    items=Shek.objects.all()
    email=request.session.get("email")
    user_obj=User.objects.get(user_email=email)
    request.session['username']=user_obj.user_name
    username=request.session.get("username")
    request.session['role']=user_obj.user_role
    role=request.session.get("role")
    # if request.session.get("project"):
    project=request.session.get("project")
    return render(request,'shekat.html',{'project':project,'username':username,'items':items,'role':role})
##############################################################################
# to delete existing m2awel
def delm2awel(request,uid):
    M2awel.objects.filter(id=uid).delete()
    # today_date=time.strftime("%d/%m/%Y")
    # if request.session.get("project"):
    project=request.session.get("project")
    pro_obj=Project.objects.get(name=project)
    persons=M2awel.objects.filter(project=pro_obj)
    email=request.session.get("email")
    user_obj=User.objects.get(user_email=email)
    request.session['username']=user_obj.user_name
    username=request.session.get("username")
    request.session['role']=user_obj.user_role
    role=request.session.get("role")
    return render(request,'m2alen.html',{'project':project,'username':username,'persons':persons,'role':role})
##############################################################################
# to edit item info
def edititem(request,uid):
    if request.method == 'POST':
        obj=Item.objects.get(id=uid)
        if request.POST.get("title"):
            obj.item_title=request.POST.get("title")
        if request.POST.get("price"):
            obj.item_price=request.POST.get("price")
        if request.POST.get("amount"):
            obj.item_amount=request.POST.get("amount")
        if request.POST.get("total"):
            obj.item_total=request.POST.get("total")
        if request.POST.get("date"):
            obj.item_date=request.POST.get("date")
        if request.POST.get("notes"):
            obj.item_description=request.POST.get("notes")
        obj.save()
        # if request.session.get("project"):
        project=request.session.get("project")
        pro_obj=Project.objects.get(name=project)
  
        items=Item.objects.filter(project=pro_obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        today_date=date.today()
        # project=request.session.get("project")
        # pro_obj=Project.objects.get(name=project)
        items=Item.objects.filter(item_date=today_date,project=pro_obj)
        all_price=0
        for item in items:
            ss=int(item.item_total.encode('utf-8'))
            all_price=all_price+ss
        # project=request.session.get("project")
        role=request.session.get("role")
        return render(request,'today.html',{'project':project,'username':username,'role':role,'items':items,'today_date':today_date,'all_price':all_price})
    else:
        obj=Item.objects.get(id=uid)
        today_date=date.today()
        if request.session.get("project"):
            project=request.session.get("project")

            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            return render(request,'edititem.html',{'project':project,'obj':obj,'today_date':today_date,'username':username,'role':role})
##############################################################################
# to edit m2awel info
def editm2awel(request,uid):
    if request.method == 'POST':
        obj=M2awel.objects.get(id=uid)
        if request.POST.get("name"):
            obj.name=request.POST.get("name")
        if request.POST.get("money"):
            obj.money=request.POST.get("money")
        if request.POST.get("job"):
            obj.job=request.POST.get("job")
        obj.save()
        # if request.session.get("project"):
        project=request.session.get("project")
        pro_obj=Project.objects.get(name=project)
        persons=M2awel.objects.filter(project=pro_obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        return render(request,'m2alen.html',{'project':project,'username':username,'persons':persons,'role':role})
    else:
        obj=M2awel.objects.get(id=uid)
        # today_date=time.strftime("%d/%m/%Y")
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        # if request.session.get("project"):
        project=request.session.get("project")
      
        role=request.session.get("role")
        return render(request,'editm2awel.html',{'project':project,'obj':obj,'username':username,'role':role})
##############################################################################
# to edit action info
def editaction(request,uid):
    if request.method == 'POST':
        obj=M2awel.objects.get(id=uid)
        action_obj=Transaction.objects.get(m2awel=obj)
        if request.POST.get("paid"):
            action_obj.action_paid=request.POST.get("paid")
        action_obj.save()
        actions=Transaction.objects.filter(m2awel=obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        # if request.session.get("project"):
        project=request.session.get("project")       
        return render(request,'viewm2awel.html',{'project':project,'username':username,'role':role,'obj':obj,'actions':actions})
    else:
        obj=M2awel.objects.get(id=uid)
        action_obj=Transaction.objects.get(m2awel=obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role") 
        # today_date=time.strftime("%d/%m/%Y")
        # if request.session.get("project"):
        project=request.session.get("project")
        return render(request,'editaction.html',{'project':project,'obj':obj,'action':action_obj,'username':username,'role':role})
#################################################################################
# to edit shek info
def editshek(request,uid):
    if request.method == 'POST':
        # if request.session.get("project"):
        project=request.session.get("project")
        pro_obj=Project.objects.get(name=project)
     
        obj=Shek.objects.get(id=uid)
        if request.POST.get("num"):
            obj.num=request.POST.get("num")
        if request.POST.get("date"):
            obj.date=request.POST.get("date")
        if request.POST.get("amount"):
            obj.amount=request.POST.get("amount")
        obj.save()
        items=Shek.objects.filter(project=pro_obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        return render(request,'shekat.html',{'project':project,'username':username,'items':items,'role':role})
    else:
        obj=Shek.objects.get(id=uid)
        # today_date=time.strftime("%d/%m/%Y")
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        # if request.session.get("project"):
        project=request.session.get("project")
        return render(request,'editshek.html',{'project':project,'obj':obj,'username':username,'role':role})
##########################################################################
# to add new action 
def addaction(request,uid):
    if request.method == 'POST':
        m2awel_obj=M2awel.objects.get(id=uid)
        i_paid=request.POST.get("paid")
        today_date=date.today()
        i_paid=int(i_paid)
        obj=Transaction(action_paid=i_paid,action_date=today_date,m2awel=m2awel_obj)
        obj.save()
        actions=Transaction.objects.filter(m2awel=m2awel_obj)
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        # if request.session.get("project"):
        project=request.session.get("project")
       
        return render(request,'viewm2awel.html',{'project':project,'username':username,'role':role,'obj':m2awel_obj,'actions':actions})
    else:
        m2awel_obj=M2awel.objects.get(id=uid)
        # today_date=time.strftime("%d/%m/%Y")
        today_date=date.today()
        project=request.session.get("project")
        email=request.session.get("email")
        user_obj=User.objects.get(user_email=email)
        request.session['username']=user_obj.user_name
        username=request.session.get("username")
        request.session['role']=user_obj.user_role
        role=request.session.get("role")
        # if request.session.get("project"):
        project=request.session.get("project")
        return render(request,'addaction.html',{'project':project,'username':username,'role':role,'obj':m2awel_obj,'today_date':today_date})
############################################################################
def sheksearch(request):
    if request.method == 'POST':
        shek_date=request.POST.get("datepicker")
        if shek_date:
            month,day,year = shek_date.split('/')
            month=month.encode('utf-8')
            day=day.encode('utf-8')
            year=year.encode('utf-8')
            print("day: ",day," month: ",month," year: ",year)
            day=int(day)
            month=int(month)
            year=int(year)
            testdate=datetime.datetime(year,month,day)
            # ss_items=Item.objects.all().values_list('item_title',flat=True)
            shekat=Shek.objects.filter(date=testdate)
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            # if request.session.get("project"):
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
            today_date=date.today()
        else:
            today_date=date.today()
            # ss_items=Item.objects.all().values_list('item_title',flat=True)
            shekat=Shek.objects.filter(date=today_date)
            email=request.session.get("email")
            user_obj=User.objects.get(user_email=email)
            request.session['username']=user_obj.user_name
            username=request.session.get("username")
            request.session['role']=user_obj.user_role
            role=request.session.get("role")
            # if request.session.get("project"):
            project=request.session.get("project")
            pro_obj=Project.objects.get(name=project)
        return render(request,'shekat.html',{'today_date':today_date,'test_date':testdate,'project':project,'username':username,'role':role,'today_date':today_date,'items':shekat})
##################################################3
# to view m2awel transactions
def viewm2awel(request,uid):
    obj=M2awel.objects.get(id=uid)
    # if request.session.get("project"):
    project=request.session.get("project")
    pro_obj=Project.objects.get(name=project)
    actions=Transaction.objects.filter(m2awel=obj)
    email=request.session.get("email")
    user_obj=User.objects.get(user_email=email)
    request.session['username']=user_obj.user_name
    username=request.session.get("username")
    request.session['role']=user_obj.user_role
    role=request.session.get("role")
    return render(request,'viewm2awel.html',{'project':project,'role':role,'username':username,'obj':obj,'actions':actions})