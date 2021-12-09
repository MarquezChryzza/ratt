from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('username','date_joined', 'last_login', 'is_student', 'is_teacher')
    search_fields = ('username', 'password')
    readonly_fields = ('date_joined', 'last_login')


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class StudentAdmin(UserAdmin):
    ordering = ('user',)
    list_display = ('firstname','lastname')
    search_fields = ('firstname', 'last_name')
    def firstname(self,account):
        return account.user.first_name
    def lastname(self,account):
        return account.user.last_name 
    readonly_fields = ()


    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 

admin.site.register(Account, AccountAdmin)

