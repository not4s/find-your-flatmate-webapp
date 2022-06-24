import django_filters
from django import forms
from .models import Post

class DateInput(forms.DateInput):
    input_type = 'date'
class PostFilter(django_filters.FilterSet):

    start_date = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    end_date = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ('start_date', 'end_date', 'search_location', 'studies_at', 'budget')