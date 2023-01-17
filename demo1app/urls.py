from django.urls import path

from demo1app import views, adminviews, studentviews, parentviews

urlpatterns = [
    path('',views.home,name='home'),
    path('login_page',views.login_page,name='login_page'),
    path('logout_page', views.logout_page, name='logout_page'),
    path('admin_page', views.admin_page, name='admin_page'),
    path('student_page', views.student_page, name='student_page'),
    path('parent_page', views.parent_page, name='parent_page'),
    path('parent_login', views.parent_login, name='parent_login'),
    path('student_login', views.student_login, name='student_login'),
    path('stud_view', adminviews.stud_view, name='stud_view'),
    path('parent_view', adminviews.parent_view, name='parent_view'),

    path('approve_student/<int:id>/',adminviews.approve_student, name='approve_student' ),
    path('reject_student/<int:id>/',adminviews.reject_student, name='reject_student' ),
    path('approve_parent/<int:id>/', adminviews.approve_parent, name='approve_parent'),
    path('reject_parent/<int:id>/', adminviews.reject_parent, name='reject_parent'),

    path('add_hostel', adminviews.add_hostel, name='add_hostel'),
    path('view_hostel', adminviews.view_hostel, name='view_hostel'),
    path('hostel_update/<int:id>/', adminviews.hostel_update, name='hostel_update'),
    path('hostel_delete/<int:id>/', adminviews.hostel_delete, name='hostel_delete'),

    path('add_food', adminviews.add_food, name='add_food'),
    path('view_food', adminviews.view_food, name='view_food'),
    path('food_update/<int:id>/', adminviews.food_update, name='food_update'),
    path('food_delete/<int:id>/', adminviews.food_delete, name='food_delete'),

    path('add_fee', adminviews.add_fee, name='add_fee'),
    path('view_fee', adminviews.view_fee, name='view_fee'),
    path('fee_update/<int:id>/', adminviews.fee_update, name='fee_update'),
    path('fee_delete/<int:id>/', adminviews.fee_delete, name='fee_delete'),

    path('add_payment', adminviews.add_payment, name='add_payment'),
    path('view_payment', adminviews.view_payment, name='view_payment'),
    path('payment_update/<int:id>/', adminviews.payment_update, name='payment_update'),
    path('payment_delete/<int:id>/', adminviews.payment_delete, name='payment_delete'),
    # path('approve_payment/<int:id>/', adminviews.approve_pay, name='approve_pay'),
    # path('reject_pay/<int:id>/', adminviews.reject_pay, name='reject_pay'),


    path('add_attendance', adminviews.add_attendance, name='add_attendance'),
    path('view_attendance', adminviews.view_attendance, name='view_attendance'),
    path('attendance_update/<int:id>/', adminviews.attendance_update, name='attendance_update'),
    path('attendance_delete/<int:id>/', adminviews.attendance_delete, name='attendance_delete'),

    path('add_staff', adminviews.add_staff, name='add_staff'),
    path('view_staff', adminviews.view_staff, name='view_staff'),
    path('staff_update/<int:id>/', adminviews.staff_update, name='staff_update'),
    path('food_delete/<int:id>/', adminviews.staff_delete, name='staff_delete'),

    path('add_noti', adminviews.add_noti, name='add_noti'),
    path('view_noti', adminviews.view_noti, name='view_noti'),
    path('noti_update/<int:id>/', adminviews.noti_update, name='noti_update'),
    path('noti_delete/<int:id>/', adminviews.noti_delete, name='noti_delete'),
    path('view_com', adminviews.view_com, name='view_com'),
    path('add_replay/<int:id>/', adminviews.add_replay,name='add_replay'),

    path('view_review',adminviews.view_review, name='view_review'),
    path('view_booking', adminviews.view_booking, name='view_booking'),


    path('view_studhostel', studentviews.view_studhostel, name='view_studhostel'),
    path('view_studatt', studentviews.view_studatt, name='view_studatt'),
    path('view_studnoti', studentviews.view_studnoti, name='view_studnoti'),
    path('view_studfee', studentviews.view_studfee, name='view_studfee'),

    path('view_studpay', studentviews.view_studpay, name='view_studpay'),
    path('approve_payment/<int:id>/', studentviews.approve_pay, name='approve_pay'),
    path('reject_pay/<int:id>/', studentviews.reject_pay, name='reject_pay'),
    path('view_studfood', studentviews.view_studfood, name='view_studfood'),

    path('add_studcom', studentviews.add_studcom, name='add_studcom'),
    path('view_studcom', studentviews.view_studcom, name='view_studcom'),
    path('update_com/<int:id>/', studentviews.update_com, name='update_com'),
    path('delete_com/<int:id>/', studentviews.delete_com, name='delete_com'),

    path('add_studreview', studentviews.add_studreview, name='add_studreview'),
    path('view_studreview', studentviews.view_studreview, name='view_studreview'),
    path('add_studbooking', studentviews.add_studbooking, name='add_studbooking'),
    path('view_studbooking', studentviews.view_studbooking, name='view_studbooking'),
    path('booking_update/<int:id>/', studentviews.booking_update, name='booking_update'),
    path('booking_delete/<int:id>/', studentviews.booking_delete, name='booking_delete'),
    path('view_studprofile', studentviews.view_studprofile, name='view_studprofile'),
    path('update_profile', studentviews.update_profile, name='update_profile'),
    # path('view_acc_delete', studentviews.view_acc_delete, name='view_acc_delete'),
    path('acc_delete', studentviews.acc_delete, name='acc_delete'),
    # path('cancel_acc', studentviews.cancel_acc, name='cancel_acc'),



    path('approve_booking/<int:id>/', adminviews.approve_booking, name='approve_booking'),
    path('reject_booking/<int:id>/', adminviews.reject_booking, name='reject_booking'),




    path('view_parent_hostel', parentviews.view_parent_hostel, name='view_parent_hostel'),
    path('view_parent_noti', parentviews.view_parent_noti, name='view_parent_noti'),
    path('view_parent_att', parentviews.view_parent_att, name='view_parent_att'),
    path('view_parent_staff', parentviews.view_parent_staff, name='view_parent_staff'),
    path('view_parent_pay', parentviews.view_parent_pay, name='view_parent_pay'),
    path('view_parent_fee', parentviews.view_parent_fee, name='view_parent_fee'),
    path('view_parent_booking', parentviews.view_parent_booking, name='view_parent_booking'),

    path('acc_delete_parent', parentviews.acc_delete_parent, name='acc_delete_parent'),

]
