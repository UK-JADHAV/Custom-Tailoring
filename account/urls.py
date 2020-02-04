from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [

    url('signup/', views.signup_view, name="signup"),
    url('login/',views.login_view, name="login"),
    url('logout/',views.logout_view, name="logout"),
    #url('skip/',views.skip_view, name="skip"),


]
