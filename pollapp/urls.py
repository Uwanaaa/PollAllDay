from . import views
from django.urls import path

app_name="pollapp"
urlpatterns = [
    #path('home/',views.greet,name='home'),
    path('<int:pk>/details',views.DetailView.as_view(),name='details'),
    path('<int:pk>/results',views.ResultView.as_view(),name='result'),
    path('<int:question_id>/vote',views.vote,name='vote'),
    path('latest/',views.latest,name='latest')
]
