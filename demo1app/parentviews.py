from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from demo1app.forms import Parent_Form
from demo1app.models import Hostal, Notification, Staff, Attendance, Payment, Fee, Booking, Parent_registration


@login_required(login_url='login_page')
def view_parent_hostel(request):
    data=Hostal.objects.all()
    return render(request, 'view_parent_hostel.html', {'data': data})

@login_required(login_url='login_page')
def view_parent_noti(request):
    data=Notification.objects.all()
    return render(request, 'view_parent_noti.html', {'data': data})

@login_required(login_url='login_page')
def view_parent_att(request):
    u = Parent_registration.objects.get(user=request.user)
    data = Attendance.objects.filter(studentname=u.student_name)
    return render(request, 'view_parent_att.html', {'data': data})

@login_required(login_url='login_page')
def view_parent_staff(request):
    data=Staff.objects.all()
    return render(request, 'view_parent_staff.html', {'data': data})

@login_required(login_url='login_page')
def view_parent_pay(request):
    u = Parent_registration.objects.get(user=request.user)
    data =Payment.objects.filter(studentname=u.student_name)
    return render(request, 'view_parent_pay.html', {'data': data})

@login_required(login_url='login_page')
def view_parent_fee(request):
    data=Fee.objects.all()
    return render(request, 'view_parent_fee.html', {'data': data})

@login_required(login_url='login_page')
def view_parent_booking(request):
    u = Parent_registration.objects.get(user=request.user)
    data = Booking.objects.filter(name=u.student_name)
    return render(request, 'view_parent_booking.html', {'data': data})


#
# @login_required(login_url='login_page')
# def view_parent_profile(request):
#         parent= Parent_registration.objects.get(user=request.user)
#         return render(request, 'view_parent_profile.html', {'parent': parent})
# #
# @login_required(login_url='login_page')
# def update_parent_profile(request):
#     pro=Parent_registration.objects.get(user=request.user)
#     form=Parent_Form(instance=pro)
#     if request.method=='POST':
#         form=Parent_Form(request.POST,request.FILES,instance=pro)
#     if form.is_valid():
#         form.save()
#         return redirect('view_parent_profile')
#     return render(request, 'update_parent_profile.html',{'form':form})

@login_required(login_url='login_page')
def acc_delete_parent(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request, 'your account deleted successfully')
        return redirect('login_page')
    return render(request,'delete_parent_acc.html')

