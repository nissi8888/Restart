
from django.contrib import admin
from django.urls import path 
from courses.views import MyCoursesList,HomePage, HomePageView , coursePage , SignupView, LoginView , signout , checkout , verifyPayment  
from codewithsamuel.settings import MEDIA_ROOT , MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomePage , name='home'),
    path('courses', HomePageView.as_view() , name='courses'),
    path('logout', signout , name='logout'),
    path('my-courses', MyCoursesList.as_view() , name='my-courses'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('login', LoginView.as_view() , name = 'login'),
    path('course/<str:slug>', coursePage , name= 'coursePage'),
    path('check-out/<str:slug>', checkout , name= 'checkpage'),
    path('verify_payment', verifyPayment , name= 'verify_payment'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)