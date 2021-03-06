from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from webapp.models import UserInfo, Post


class UserInline(admin.StackedInline):
    model = UserInfo
    fields = ['phone', 'friends', 'photo']

class UserInfoAdmin(UserAdmin):
    inlines = [UserInline]

admin.site.unregister(User)
admin.site.register(User, UserInfoAdmin)
admin.site.register(Post)
