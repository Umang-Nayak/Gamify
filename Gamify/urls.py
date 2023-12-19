from django.contrib import admin
from django.urls import path
from Gamify_Admin import views


urlpatterns = [

    # Super User Page
    path('admin/', admin.site.urls),


    # Registration - Login - Forgot Password
    path('admin_register/', views.register_user),
    path('admin_login/', views.login_user),
    path('forgot_password/', views.user_forgot_password),
    path('otp/', views.user_otp),
    path('forgot_password_verification/', views.sendotp),
    path('otp_verification/', views.set_password),

    # Show Data
    path('city/', views.show_city),
    path('user/', views.show_user),
    path('company/', views.show_company),
    path('type/', views.show_type),
    path('game/', views.show_game),
    path('wishlist/', views.show_wishlist),
    path('order/', views.show_order),
    path('order_detail/', views.show_order_detail),
    path('feedback/', views.show_feedback),
    path('cart/', views.show_cart),
    path('dashboard/',views.show_dashboard),
    path('profile/',views.show_profile),



    # Delete Data
    path('delete_city/<int:id>', views.destroy_city),
    path('delete_user/<int:id>', views.destroy_user),
    path('delete_company/<int:id>', views.destroy_company),
    path('delete_type/<int:id>', views.destroy_type),
    path('delete_game/<int:id>', views.destroy_game),

    # Update Data
    path('update_city/<int:id>', views.change_city),
    # path('update_user/<int:id>', views.change_user),
    path('update_company/<int:id>', views.change_company),
    path('update_type/<int:id>', views.change_type),
    path('update_game/<int:id>', views.change_game),


    # Insert Data
    path('insert_city/', views.enter_city),
    path('insert_company/', views.enter_company),
    path('insert_type/', views.enter_type),
    path('insert_game/', views.enter_game),
]
