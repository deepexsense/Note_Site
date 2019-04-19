from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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


class NotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'user_notes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NotesView, self).get_context_data(**kwargs)
        order_by = self.request.GET.get('order_by', default='title_lower')
        direction = self.request.GET.get('direction')
        context['order_by'] = order_by
        context['direction'] = direction
        if direction == 'desc':
            order_by = '-{}'.format(order_by)
        context['filter'] = NoteFilter(self.request.GET, queryset=Note.objects.filter(user=self.request.user).
                                       extra(select={'title_lower': 'lower(title)'}).
                                       order_by(order_by))
        return context


class AjaxableNotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'ajax_notes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AjaxableNotesView, self).get_context_data(**kwargs)
        order_by = self.request.GET.get('order_by', default='title_lower')
        direction = self.request.GET.get('direction')
        context['order_by'] = order_by
        context['direction'] = direction
        if direction == 'desc':
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


class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/'

    template_name = 'registration/login.html'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'registration/logout.html', {})


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
    success_url = '/my_notes'

    def get_object(self, queryset=None):
        note = Note.objects.get(id=self.kwargs["id"])
        return note


class NoteDeletingView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'delete_confirmation.html'
    success_url = '/my_notes/delete_success'

    def get_object(self, queryset=None):
        note = Note.objects.get(note_id=self.kwargs["note_id"])
        return note


class DeleteSuccessView(TemplateView):
    template_name = 'delete_success.html'


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

