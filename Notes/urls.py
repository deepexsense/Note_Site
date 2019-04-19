from django.conf.urls import url

from Notes import views

urlpatterns = [
    url(r'^$', views.TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^my_notes/$', views.NotesView.as_view(), name='my_notes'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^registration_success/$', views.RegistrationSuccessView.as_view(), name='registration_success'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^(?P<id>[0-9a-f-]+)/$', views.NoteDetailView.as_view(), name='detail'),
    url(r'^my_notes/new/$', views.NoteFormView.as_view(),name='note_new'),
    url(r'^my_notes/edit/(?P<id>[0-9a-f-]+)/$', views.NoteEditingView.as_view(), name='note_edit'),
    url(r'^my_notes/delete/(?P<id>[0-9a-f-]+)/$', views.NoteDeletingView.as_view(), name='note_delete'),
    url(r'^my_notes/delete_success/$', views.DeleteSuccessView.as_view(), name='note_delete_success'),
    url(r'^my_notes/ajax/$', views.AjaxableNotesView.as_view(), name='ajax_notes'),
]

