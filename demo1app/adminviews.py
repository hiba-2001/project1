from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from demo1app.forms import Hostel_form, Food_form, Fee_form, Payment_form, Attendance_form, Staff_form, \
    Notification_form, Repaly_form
from demo1app.models import Student_registration, Parent_registration, Hostal, Food, Fee, Payment, Attendance, Staff, \
    Notification, Complaint, Review, Booking

@login_required(login_url='login_page')
def stud_view(request):
    data=Student_registration.objects.all()
    return render(request, 'view.html',{'data':data})

@login_required(login_url='login_page')
def parent_view(request):
    data=Parent_registration.objects.all()
    return render(request, 'pview.html',{'data':data})

@login_required(login_url='login_page')
def approve_student(request, id):
    student1=Student_registration.objects.get(user_id=id)
    student1.approval_status = 1
    student1.save()
    messages.info(request,"Student approved succesfully")
    return redirect('stud_view')

@login_required(login_url='login_page')
def approve_parent(request, id):
    parent1=Parent_registration.objects.get(user_id=id)
    parent1.approval_status = 1
    parent1.save()
    messages.info(request, "Parent approved succesfully")
    return redirect('parent_view')

@login_required(login_url='login_page')
def reject_student(request, id):
    student1=Student_registration.objects.get(user_id=id)
    # if request.method=='POST':
    student1.approval_status = 2
    student1.save()
    messages.info(request,"Rejected student registration")
    return redirect('stud_view')

@login_required(login_url='login_page')
def reject_parent(request, id):
    parent1=Parent_registration.objects.get(user_id=id)
    parent1.approval_status = 2
    parent1.save()
    messages.info(request, "Parent rejected succesfully")
    return redirect('parent_view')

@login_required(login_url='login_page')
def add_hostel(request):
    form= Hostel_form()
    if request.method=='POST':
        form=Hostel_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_hostel')
    return render(request, 'add_hostel.html',{'form':form})

@login_required(login_url='login_page')
def view_hostel(request):
    data=Hostal.objects.all()
    return render(request, 'view_hostel.html', {'data': data})

@login_required(login_url='login_page')
def hostel_update(request,id):
    host1=Hostal.objects.get(id=id)
    form=Hostel_form(instance=host1)
    if request.method=='POST':
        form=Hostel_form(request.POST,request.FILES,instance=host1)
    if form.is_valid():
        form.save()
        return redirect('view_hostel')
    return render(request, 'add_hostel.html',{'form':form})


@login_required(login_url='login_page')
def hostel_delete(request,id):

        Hostal.objects.get(id=id).delete()
        return redirect('view_hostel')


@login_required(login_url='login_page')
def add_food(request):
    form= Food_form()
    if request.method=='POST':
        form=Food_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_food')
    return render(request, 'add_food.html',{'form':form})

@login_required(login_url='login_page')
def view_food(request):
    data=Food.objects.all()
    return render(request, 'view_food.html', {'data': data})

@login_required(login_url='login_page')
def food_update(request,id):
    food1=Food.objects.get(id=id)
    form=Food_form(instance=food1)
    if request.method=='POST':
        form=Food_form(request.POST,instance=food1)
    if form.is_valid():
        form.save()
        return redirect('view_food')
    return render(request, 'add_food.html',{'form':form})


@login_required(login_url='login_page')
def food_delete(request,id):

        Food.objects.get(id=id).delete()
        return redirect('view_food')

@login_required(login_url='login_page')
def add_fee(request):
    form= Fee_form()
    if request.method=='POST':
        form=Fee_form(request.POST )
        if form.is_valid():
            form.save()
            return redirect('view_fee')
    return render(request, 'add_fee.html',{'form':form})

@login_required(login_url='login_page')
def view_fee(request):
    data=Fee.objects.all()
    return render(request, 'view_fee.html', {'data': data})

@login_required(login_url='login_page')
def fee_update(request,id):
    fee1=Fee.objects.get(id=id)
    form=Fee_form(instance=fee1)
    if request.method=='POST':
        form=Fee_form(request.POST,instance=fee1)
    if form.is_valid():
        form.save()
        return redirect('view_fee')
    return render(request, 'add_fee.html',{'form':form})


@login_required(login_url='login_page')
def fee_delete(request,id):

        Fee.objects.get(id=id).delete()
        return redirect('view_fee')

@login_required(login_url='login_pa ge')
def add_payment(request):
    form= Payment_form()
    if request.method=='POST':
        form=Payment_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_payment')
    return render(request, 'add_payment.html',{'form':form})

@login_required(login_url='login_page')
def view_payment(request):
    data=Payment.objects.all()
    return render(request, 'view_payment.html', {'data': data})


@login_required(login_url='login_page')
def payment_update(request,id):
    pay1=Payment.objects.get(id=id)
    form=Payment_form(instance=pay1)
    if request.method=='POST':
        form=Payment_form(request.POST,instance=pay1)
    if form.is_valid():
        form.save()
        return redirect('view_payment')
    return render(request, 'add_payment.html',{'form':form})


@login_required(login_url='login_page')
def payment_delete(request,id):

        Payment.objects.get(id=id).delete()
        return redirect('view_payment')

#
#
# @login_required(login_url='login_page')
# def approve_pay(request, id):
#     pay1=Payment.objects.get(id=id)
#     pay1.paymentstatus = 1
#     pay1.save()
#     messages.info(request,"Student paid succesfully")
#     return redirect('view_payment')
#
#
# @login_required(login_url='login_page')
# def reject_pay(request, id):
#     pay1=Payment.objects.get(id=id)
#     pay1.paymentstatus = 2
#     pay1.save()
#     messages.info(request,"not paid")
#     return redirect('view_payment')




@login_required(login_url='login_page')
def add_attendance(request):
    form= Attendance_form()
    if request.method=='POST':
        form=Attendance_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_attendance')
    return render(request, 'add_food.html',{'form':form})

@login_required(login_url='login_page')
def view_attendance(request):
    data=Attendance.objects.all()
    return render(request, 'view_attendance.html', {'data': data})

@login_required(login_url='login_page')
def attendance_update(request,id):
    att=Attendance.objects.get(id=id)
    form=Attendance_form(instance=att)
    if request.method=='POST':
        form=Attendance_form(request.POST,instance=att)
    if form.is_valid():
        form.save()
        return redirect('view_attendance')
    return render(request, 'add_attendance.html',{'form':form})


@login_required(login_url='login_page')
def attendance_delete(request,id):

        Attendance.objects.get(id=id).delete()
        return redirect('view_attendance')

@login_required(login_url='login_page')
def add_staff(request):
    form=Staff_form()
    if request.method=='POST':
        form=Staff_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_staff')
    return render(request, 'add_staff.html',{'form':form})

@login_required(login_url='login_page')
def view_staff(request):
    data=Staff.objects.all()
    return render(request, 'view_staff.html', {'data': data})

@login_required(login_url='login_page')
def staff_update(request,id):
    stf=Staff.objects.get(id=id)
    form=Staff_form(instance=stf)
    if request.method=='POST':
        form=Staff_form(request.POST,instance=stf)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request, 'add_staff.html',{'form':form})


@login_required(login_url='login_page')
def staff_delete(request,id):

        Staff.objects.get(id=id).delete()
        return redirect('view_staff')


@login_required(login_url='login_page')
def add_noti(request):
    form= Notification_form()
    if request.method=='POST':
        form=Notification_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_noti')
    return render(request, 'add_noti.html',{'form':form})

@login_required(login_url='login_page')
def view_noti(request):
    data=Notification.objects.all()
    return render(request, 'view_noti.html', {'data': data})

@login_required(login_url='login_page')
def noti_update(request,id):
    noti=Notification.objects.get(id=id)
    form=Notification_form(instance=noti)
    if request.method=='POST':
        form=Notification_form(request.POST,instance=noti)
    if form.is_valid():
        form.save()
        return redirect('view_noti')
    return render(request, 'add_noti.html',{'form':form})


@login_required(login_url='login_page')
def noti_delete(request,id):

        Notification.objects.get(id=id).delete()
        return redirect('view_noti')


@login_required(login_url='login_page')
def view_com(request):
    data=Complaint.objects.all()
    return render(request, 'view_com.html', {'data': data})

@login_required(login_url='login_page')
def view_review(request):
    data=Review.objects.all()
    return render(request, 'view_review.html', {'data': data})

@login_required(login_url='login_page')
def view_booking(request):
    data=Booking.objects.all()
    return render(request, 'view_booking.html', {'data': data})

@login_required(login_url='login_page')
def approve_booking(request, id):
    booking1=Booking.objects.get(id=id)
    booking1.status = 1
    booking1.save()
    messages.info(request,"Student approved succesfully")
    return redirect('view_booking')

@login_required(login_url='login_page')
def reject_booking(request, id):
    booking1=Booking.objects.get(id=id)

    booking1.status = 2
    booking1.save()
    messages.info(request,"Rejected student registration")
    return redirect('view_booking')

@login_required(login_url='login_page')
def add_replay(request,id):
    f=Complaint.objects.get(id=id)
    if request.method == 'POST':
        r=request.POST.get('replay')
        f.replay=r
        f.save()
        return redirect('view_com')
    return render(request, 'add_replay.html', {'f':f})


