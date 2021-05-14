# Define differents path in our APP
from django.urls import path
from . import views
# which APP will create a new URL from the reverse function
app_name = 'user'
# url path
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
