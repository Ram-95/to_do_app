from django.contrib import admin
from . models import Profile
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Overrides the details of Profile Model in Admin'''
    # Displays the User ID, User Name and the No.of Tasks of a User
    list_display = ("profile_id", "user_id", "user", "view_tasks_link")
    # Adding a Filter by Username
    list_filter = ("user",)
    # Adding a search functionality to Admin - Searches based on the first name of user
    search_fields = ("first_name__startswith", )

    def view_tasks_link(self, obj):
        '''Returns the Link to the Tasks page of a User'''
        # Gets the count of the Tasks of a User
        count = obj.user.task_set.count()
        # Gets the link to the Tasks of a User
        url = (reverse("admin:to_do_task_changelist") + "?" +
               urlencode({"author__id": f"{obj.user.id}"}))
        
        # Shows the link to the 'Tasks' page of the User
        return format_html('<a href="{}">{} Tasks</a>', url, count)

    # Renaming - Name used in the Admin portal
    view_tasks_link.short_description = "No. of Tasks"


    def user_id(self, obj):
        '''Returns the User ID of the current profile'''
        return obj.user.id
    
    
    def profile_id(self, obj):
        '''Returns the Profile ID of the current profile'''
        return obj.id
