from django.contrib import admin

from accounts.models import UserAction, Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    """
    Admin class to customize the display of Profile objects in the Django admin interface.

    fields: Specifies the fields to be displayed on the form when adding or editing a Profile.
    list_display: Defines the columns to be displayed in the list view of the Profile objects.
    """

    fields = ('user', 'image')
    list_display = ('user', 'image')


class UserActionAdmin(admin.ModelAdmin):
    """
    Django admin model configuration for the UserAction model.

    Fields:
    - fields: Specifies the fields to be displayed on the form in the Django admin.
    - readonly_fields: Defines which fields should be read-only in the admin interface.
    - list_display: Specifies the fields to be displayed in the list view of the admin interface.
    """

    fields = ('user', 'action')
    readonly_fields = ('write_date', )
    list_display = ('user', 'write_date', 'action')


admin.site.register(Profile, ProfileAdmin)

admin.site.register(UserAction, UserActionAdmin)
