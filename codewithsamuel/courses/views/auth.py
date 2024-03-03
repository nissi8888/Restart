from django.shortcuts import render , redirect
from django.contrib.auth import logout , login
from courses.forms import RegistrationForm , LoginForm 
from django.views import View
from django.views.generic.edit import FormView
from django.utils.html import format_html

class SignupView(FormView):
    template_name="courses/signup.html" 
    form_class = RegistrationForm
    success_url  = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    

class LoginView(FormView):
    template_name="courses/login.html" 
    form_class = LoginForm
    success_url  = '/'

    def form_valid(self, form):
        login(self.request , form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)


def signout(request ):
    logout(request)
    return redirect("home")
    
'''
class SignupView(View):
    def get(self, request):
        form = RegistrationForm ()
        print("Response From Class Based")
        return render(request , 
        template_name="courses/signup.html" , context= {'form' : form})
    
    def post(self, request):
        form = RegistrationForm (request.POST)
        if(form.is_valid()):
            user =  form.save()
            if(user is not None):
               return redirect('login')
        return render(request , 
        template_name="courses/signup.html" , context= {'form' : form}) 

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request , 
         template_name="courses/login.html" , context=context)
    

    def post(self , request):
        form = LoginForm(request = request, data=request.POST)
        context = {
            "form" : form
        }
        if(form.is_valid()):
           return redirect("home")
        return render(request , 
           template_name="courses/login.html" , context=context)

           

def signout(request):
    logout(request)
    return redirect("home")
'''