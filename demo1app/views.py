from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from demo1app.forms import user_register, Student_Form, Parent_Form


# Create your views here.

def home(request):
    return render(request, 'index.html')


def login_page(request):
        if request.method == 'POST':
            username = request.POST.get('uname')
            password = request.POST.get('pass')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('admin_page')
                elif user is not None and user.is_student:
                    if user.student.approval_status==True:
                        login(request,user)
                        return redirect('student_page')
                elif user is not None and user.is_parent:
                    if user.parent.approval_status==True:
                        login(request,user)
                        return redirect('parent_page')

            else:
                messages.info(request, 'invalid credentials')
        return render(request,'login.html')

@login_required(login_url='login_page')
def admin_page(request):

    return render(request, 'admin_page.html')

@login_required(login_url='login_page')
def student_page(request):

    return render(request, 'student_page.html')

@login_required(login_url='login_page')
def parent_page(request):

    return render(request, 'parent_page.html')

def parent_login(request):
    u_form = user_register()
    p_form = Parent_Form()
    if request.method == "POST":
        u_form = user_register(request.POST)
        p_form = Parent_Form(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save(commit=False)
            user.is_parent = True
            user.save()
            parent = p_form.save(commit=False)
            parent.user = user
            parent.save()
            messages.info(request, 'parent registration successful')
            return redirect('login_page')

    return render(request, 'parent_login.html', {'u_form': u_form, 'p_form': p_form})


def student_login(request):
    u_form= user_register()
    s_form= Student_Form()
    if request.method=="POST":
        u_form=user_register(request.POST)
        s_form=Student_Form(request.POST,request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user=u_form.save(commit=False)
            user.is_student=True
            user.save()
            student=s_form.save(commit=False)
            student.user=user
            student.save()
            messages.info(request, 'student registration successful')
            return redirect ('login_page')

    return render(request, 'student_login.html',{'u_form':u_form,'s_form':s_form})

@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return redirect('login_page')

