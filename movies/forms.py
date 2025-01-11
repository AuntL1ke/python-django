from django import forms
from movies.models import Movie


class CreateMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


class EditMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            "position": forms.Select(attrs={"class": "form-select"})
        }