from django.conf.urls import url

from Notes import views

urlpatterns = [
    url(r'^$', views.TemplateView.as_view(template_name='base.html'), name='index'),
    url(r'^home/$', views.TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^my_notes/$', views.NotesView.as_view(), name='my_notes'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^registration_success/$', views.RegistrationSuccessView.as_view(), name='registration_success'),
    url(r'^login/$', views.SignInFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^note/(?P<id>[0-9]+)/$', views.NoteDetailView.as_view(), name='detail'),
    url(r'^note/(?P<note_id>[0-9a-f-]+)/$', views.NotePublicView.as_view(), name='note_uuid_url'),
    url(r'^my_notes/new/$', views.NoteFormView.as_view(), name='note_new'),
    url(r'^my_notes/edit/(?P<id>[0-9]+)/$', views.NoteEditingView.as_view(), name='note_edit'),
    url(r'^my_notes/delete/(?P<id>[0-9a-f-]+)/$', views.NoteDeletingView.as_view(), name='note_delete'),
    url(r'^my_notes/ajax/$', views.AjaxableNotesView.as_view(), name='ajax_notes_filter'),
    url(r'^my_notes/ajax/(?P<id>[0-9]+)/link/$', views.NoteLockedView.as_view(), name='locked_note'),
    # url(r'^login_error/$', views.TemplateView.as_view(template_name='registration/login_error.html'), name='login_error'),
    # url(r'^my_notes/ajax/validate_username/$', views.validate_username, name='validate_username'),
]

