import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from demo1app.models import Student_registration, Parent_registration, Login_view, Hostal, Food, Fee, Attendance, \
    Payment, Notification, Complaint, Review, Booking, Staff

class DateInput(forms.DateInput):
    input_type = 'date'

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('this is not a valid phone number')

class user_register(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class Student_Form(forms.ModelForm):
    phone_no = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$',message='Please Enter a Valid Email')])
    class Meta:
        model = Student_registration
        exclude = ("user","approval_status",)
def clean_email(self):
    mail = self.cleaned_data["email"]
    parent_email = Parent_registration.objects.filter(email=mail)
    student_email = Student_registration.objects.filter(email=mail)
    if parent_email.exists():
        raise forms.ValidationError("this email already registered")
    if student_email.exists():
        raise forms.ValidationError("this email already registered")
    return mail

def clean_phone_no(self):
    phone = self.cleaned_data["email"]
    parent_phone_no = Parent_registration.objects.filter(phone_no=phone)
    student_phone_no = Student_registration.objects.filter(phone_no=phone)
    if parent_phone_no.exists():
        raise forms.ValidationError("this email already registered")
    if student_phone_no.exists():
        raise forms.ValidationError("this email already registered")
    return phone




class Parent_Form(forms.ModelForm):
    phone_no = forms.CharField(validators=[phone_number_validator])
    email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$',message='Please Enter a Valid Email')])
    class Meta:
        model = Parent_registration
        fields = "__all__"
        exclude = ("user","approval_status",)

class Hostel_form(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = Hostal
        fields = "__all__"


class Food_form(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class Fee_form(forms.ModelForm):

   class Meta:
        model = Fee
        fields = "__all__"

class Payment_form(forms.ModelForm):
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Payment
        exclude = ("paymentstatus",)

att_choice=(
    ('present','present'),
    ('absent','absent')
)

class Attendance_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    status=forms.ChoiceField(choices=att_choice,widget=forms.RadioSelect)
    class Meta:
        model = Attendance
        fields = "__all__"


class Staff_form(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = Staff
        fields = "__all__"


class Notification_form(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model = Notification
        fields = "__all__"


class Complaint_form(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Complaint
        exclude = ('replay','user',)

class Repaly_form(forms.ModelForm):

    class Meta:
        model = Complaint

        exclude = ('user','date','complaint',)


class Review_form(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class Booking_form(forms.ModelForm):
    date_joining=forms.DateField(widget=DateInput)
    booking_date=forms.DateField(widget=DateInput)
    class Meta:
        model = Booking
        fields = "__all__"
        exclude = ('status',)