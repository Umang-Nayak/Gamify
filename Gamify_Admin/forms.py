from django import forms
from Gamify_Admin.models import GamifyUser


class GamifyUserForm(forms.ModelForm):
    class Meta:
        model = GamifyUser
        fields = ["user_first_name", "user_last_name",
                  "user_date_of_birth", "user_contact",
                  "user_email", "user_password",
                  "is_admin", "city_id"]
