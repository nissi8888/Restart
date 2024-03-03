from django.shortcuts import render
from django.shortcuts import HttpResponse
from courses.models import Course
from django.views.generic import ListView


class HomePageView(ListView):
    template_name = "courses/courses.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'

def HomePage(request):
    return render(request , template_name="courses/home.html")

