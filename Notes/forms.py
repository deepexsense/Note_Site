from django import forms


from Notes.models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'text', 'date', 'category', 'favorite',)
