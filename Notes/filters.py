import django_filters
from django.forms import TextInput
from django_filters.widgets import LinkWidget

from Notes.models import Note


class NoteFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains',
                                      widget=TextInput(attrs={'placeholder': 'Title'}))
    date = django_filters.IsoDateTimeFilter(widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}))

    class Meta:
        model = Note
        fields = ["title", "date", "category", "favorite", ]
