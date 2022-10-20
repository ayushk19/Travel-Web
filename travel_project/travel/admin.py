from django.contrib import admin

from .models import ContactUs, Signup_login
# from .models import Signup_login

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(Signup_login)