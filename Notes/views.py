from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, FormView, DetailView, UpdateView, DeleteView
from django.views.generic.base import View
from Notes.filters import NoteFilter
from Notes.forms import NoteForm
from .models import Note


class NoteDetailView(DetailView):
    template_name = 'detail.html'

    def get_object(self, queryset=None):
        note = Note.objects.get(id=self.kwargs['id'])
        return note


class NotePublicView(DetailView):
    template_name = 'public.html'

    def get_object(self, queryset=None):
        note = get_object_or_404(Note, note_id=self.kwargs['note_id'])
        if note.is_locked:
            raise Http404("You have no permissions for this note")
        return note


class NotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'user_notes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NotesView, self).get_context_data(**kwargs)
        context['filter'] = NoteFilter(self.request.GET, queryset=Note.objects.filter(user=self.request.user))
        return context


class AjaxableNotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'ajax_notes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AjaxableNotesView, self).get_context_data(**kwargs)
        order_by = self.request.GET.get('order_by')
        direction = self.request.GET.get('direction')
        context['order_by'] = order_by
        context['direction'] = direction
        if direction == 'descending':
            order_by = '-{}'.format(order_by)
        context['filter'] = NoteFilter(self.request.GET, queryset=Note.objects.filter(user=self.request.user).
                                       extra(select={'title_lower': 'lower(title)'}).
                                       order_by(order_by))
        return context


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/registration_success/'
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class RegistrationSuccessView(TemplateView):
    template_name = 'registration/registration_success.html'


class SignInFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/'

    template_name = 'registration/login.html'

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if user:
            login(self.request, user)
        return super(SignInFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'base.html', {})


class NoteFormView(LoginRequiredMixin, FormView):
    form_class = NoteForm
    success_url = '/'

    template_name = 'new_note.html'

    def form_valid(self, form):
        note = form.save(commit=False)
        note.user = self.request.user
        note.save()
        return super(NoteFormView, self).form_valid(form)


class NoteEditingView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'edit_note.html'
    success_url = '/'

    def get_object(self, queryset=None):
        note = Note.objects.get(id=self.kwargs["id"])
        return note


class NoteDeletingView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'delete_confirmation.html'
    success_url = '/'

    def get_object(self, queryset=None):
        note = Note.objects.get(id=self.kwargs["id"])
        return note


@method_decorator(csrf_exempt, 'dispatch')
class NoteLockedView(View):

    def post(self, request, id):
        note = Note.objects.get(id=self.kwargs["id"])
        note.is_locked = not note.is_locked
        note.save()
        return HttpResponse()
