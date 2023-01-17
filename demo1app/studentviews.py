from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from demo1app.forms import Complaint_form, Review_form, Booking_form, Student_Form, Payment_form
from demo1app.models import Hostal, Attendance, Notification, Payment, Fee, Food, Complaint, Review, Booking, \
    Student_registration

@login_required(login_url='login_page')
def view_studhostel(request):
    data=Hostal.objects.all()
    return render(request, 'view_studhostel.html', {'data': data})

@login_required(login_url='login_page')
def view_studatt(request):
    u=Student_registration.objects.get(user=request.user)
    data=Attendance.objects.filter(studentname=u)
    return render(request, 'view_studatt.html', {'data': data})

@login_required(login_url='login_page')
def view_studnoti(request):
    data=Notification.objects.all()
    return render(request, 'view_studnoti.html', {'data': data})

@login_required(login_url='login_page')
def view_studfee(request):
    data=Fee.objects.all()
    return render(request, 'view_studfee.html', {'data': data})

#
# @login_required(login_url='login_page')
# def add_payment(request):
#     form= Payment_form()
#     if request.method=='POST':
#         form=Payment_form(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('view_studpay')
#     return render(request, 'add_payment.html',{'form':form})


@login_required(login_url='login_page')
def view_studpay(request):
    data=Payment.objects.all()
    return render(request, 'view_studpay.html', {'data': data})


@login_required(login_url='login_page')
def approve_pay(request, id):
    pay1=Payment.objects.get(id=id)
    pay1.paymentstatus = 1
    pay1.save()
    messages.info(request,"Student paid succesfully")
    return redirect('view_studpay')


@login_required(login_url='login_page')
def reject_pay(request, id):
    pay1=Payment.objects.get(id=id)
    pay1.paymentstatus = 2
    pay1.save()
    messages.info(request,"not paid")
    return redirect('view_studpay')


@login_required(login_url='login_page')
def view_studfood(request):
    data=Food.objects.all()
    return render(request, 'view_studfood.html', {'data': data})

@login_required(login_url='login_page')
def add_studcom(request):
    form= Complaint_form()
    u=request.user
    if request.method=='POST':
        form=Complaint_form(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('view_studcom')
    return render(request, 'add_studcom.html',{'form':form})

@login_required(login_url='login_page')
def view_studcom(request):
    u = Student_registration.objects.get(user=request.user)
    data=Complaint.objects.filter(user=request.user)
    return render(request, 'view_studcom.html', {'data': data})


@login_required(login_url='login_page')
def update_com(request,id):
    com=Complaint.objects.get(id=id)
    form=Complaint_form(instance=com)
    if request.method=='POST':
        form=Complaint_form(request.POST,instance=com)
    if form.is_valid():
        form.save()
        return redirect('view_studcom')
    return render(request, 'add_studcom.html',{'form':form})


@login_required(login_url='login_page')
def delete_com(request,id):

        Complaint.objects.get(id=id).delete()
        return redirect('view_studcom')


@login_required(login_url='login_page')
def add_studreview(request):
    form= Review_form()
    if request.method=='POST':
        form=Review_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_studreview')
    return render(request, 'add_studreview.html',{'form':form})

@login_required(login_url='login_page')
def view_studreview(request):
    u = Student_registration.objects.get(user=request.user)
    data=Review.objects.filter(name=u)
    return render(request, 'view_studreview.html', {'data': data})


@login_required(login_url='login_page')
def add_studbooking(request):
    form= Booking_form()
    if request.method=='POST':
        form=Booking_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_page')
    return render(request, 'add_studbooking.html',{'form':form})

@login_required(login_url='login_page')
def view_studbooking(request):
    u = Student_registration.objects.get(user=request.user)
    data=Booking.objects.filter(name=u)
    return render(request, 'view_studbooking.html', {'data': data})

@login_required(login_url='login_page')
def booking_update(request,id):
    book=Booking.objects.get(id=id)
    form=Booking_form(instance=book)
    if request.method=='POST':
        form=Booking_form(request.POST,instance=book)
    if form.is_valid():
        form.save()
        return redirect('view_studbooking')
    return render(request, 'add_studbooking.html',{'form':form})


@login_required(login_url='login_page')
def booking_delete(request,id):

        Booking.objects.get(id=id).delete()
        return redirect('view_studbooking')

@login_required(login_url='login_page')
def view_studprofile(request):
        student= Student_registration.objects.get(user=request.user)
        return render(request, 'view_studprofile.html', {'student': student})

@login_required(login_url='login_page')
def update_profile(request):
    pro=Student_registration.objects.get(user=request.user)
    form=Student_Form(instance=pro)
    if request.method=='POST':
        form=Student_Form(request.POST,request.FILES,instance=pro)
    if form.is_valid():
        form.save()
        return redirect('view_studprofile')
    return render(request, 'update_profile.html',{'form':form})

#
# def view_acc_delete(request):
#     return render(request, 'delete_acc.html')

#
# def cancel_acc(request):
#     return redirect('student_page')


@login_required(login_url='login_page')
def acc_delete(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request, 'your account deleted successfully')
        return redirect('login_page')
    return render(request,'delete_acc.html')

