from django.urls import path
from .views import MainPage, ListPage, QuestionFormView

urlpatterns = [
    path('', MainPage, name='main_page'),
    path('list/', ListPage, name='list_page'),
    path('feedback/', QuestionFormView.as_view(), name='feedback')
]
