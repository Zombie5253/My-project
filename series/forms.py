from django import forms
from .models import *

#add movie form
class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('name', 'director', 'cast', 'description', 'release_Date' ,'seasons' ,'image')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("comment", "rating")        