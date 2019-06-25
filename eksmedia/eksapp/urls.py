from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'eksapp'

urlpatterns=[
    path('comics/',views.comical,name='comical'),
    path('forum/',views.forum_page,name='forum_page'),
    path('peeps/',views.peeps,name='peeps'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
]
