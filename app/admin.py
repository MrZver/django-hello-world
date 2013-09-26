from django.contrib import admin
from app.models import User
from app.models import Message

# admin.site.register(User)
admin.site.register(Message)


class UserAdmin(admin.ModelAdmin):
    # fields = ['username', 'email', 'date_created']
    list_display = ('username', 'email', 'date_created')

admin.site.register(User, UserAdmin)
