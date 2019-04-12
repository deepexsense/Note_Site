import django_filters

from Notes.models import Note


class NoteFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Note
        fields = ["title", "date", "category", "favorite", ]
