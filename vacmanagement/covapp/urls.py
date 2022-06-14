from django.urls import path

from .views import userprofile
from .views import vacregistration
from .views import certificatepage
from .views import editdetails
from .views import delete_details
from .views import login_page
from .views import register_page
from .views import logout_user

urlpatterns = [
    path('', userprofile, name = 'userProfile'),
    path('vac-registration', vacregistration, name = 'vacRegistration'),
    path('my-certificate/<str:pk>', certificatepage, name = 'certificate'),
    path('edit-details/<str:pk>', editdetails, name = "editDetails"),
    path('delete-details/<str:pk>', delete_details, name = "deleteDetails"),
    path('login/', login_page, name = 'loginPage'),
    path('signup/',  register_page, name = 'registerPage'),
    path('logout/,', logout_user, name='logout')
]