from django.contrib import admin
from .models import Listing,UserProfile,userwishlist

admin.site.register(UserProfile)
admin.site.register(Listing)
admin.site.register(userwishlist)

# Register your models here.
