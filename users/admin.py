from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'user_type')
    search_fields = ('username', 'email')
    list_filter = ('user_type',)