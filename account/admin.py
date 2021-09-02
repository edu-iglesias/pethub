from django.contrib import admin

# Register your models here.
from account.models import Profile

# class UserFilter(AutocompleteFilter):
#     user = 'User' # display title
#     field_name = 'user' # name of the foreign key field

class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "contact_number",
        "house_address",
        "city",
        "postal_code",
        "preference_tag",
    ]


    search_fields = [
        "id",
        "user",
    ]

admin.site.register(Profile, ProfileAdmin)
