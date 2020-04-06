from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import signupfunc, loginfunc,BoardCreate,logoutfunc,goodfunc,myprofilefunc,TopicList,UserRegisterView,profilefunc,BoardDelete,PostEdit,ProfileEdit

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('', TopicList.as_view(), name='list'),
    path('about/', TemplateView.as_view(template_name='templates/about.html'), name='about'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('delete/<int:pk>', BoardDelete.as_view(), name='delete'),
    path('post_edit/<int:pk>', PostEdit.as_view(), name='post_edit'),
    path('profile_edit/<int:pk>', ProfileEdit.as_view(), name='profile_edit'),
    path('logout/', logoutfunc, name='logout'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('allprofile/<int:pk>', profilefunc, name='allprofile'),
    path('profile/', myprofilefunc, name='profile'),
    path('register/', views.UserRegisterView.as_view(), name="register"),
]