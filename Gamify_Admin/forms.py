from django import forms
from Gamify_Admin.models import GamifyUser, City, Company, Type, Game


class GamifyUserForm(forms.ModelForm):
    class Meta:
        model = GamifyUser
        fields = ["user_first_name", "user_last_name",
                  "user_date_of_birth", "user_contact",
                  "user_email", "user_password",
                  "is_admin", "city_id"]


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["city_name"]

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["company_name", "company_description"]

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ["type_name"]


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["game_name","game_version","game_image",
                  "game_price","game_launch_date","game_quantity",
                  "game_description","is_available", "company_id", "type_id" ]

