from django.urls import path
from todolist import views

app_name='todolist'
urlpatterns = [
    # ex: /todo/
    path('', views.IndexView.as_view(), name='IndexView'),

    # ex: /todo/1/
    path('<int:pk>/', views.ListDetailView.as_view(), name='ListDetailView'),

    # ex: /todo/1/submit
    path('<int:todolist_id>/submit/', views.submitForm, name='submitForm'),

    # ex: /todo/1/result/
    path('<int:todolist_id>/result/', views.result, name='result'),
    ]


#{% url todolist:submitForm todolist.id %}
