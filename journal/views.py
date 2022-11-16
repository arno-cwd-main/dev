
from django.shortcuts import redirect, render

from django.http import HttpResponse


from .forms import CreateUserForm, LoginForm, ThoughtPostForm, ThoughtUpdateForm, UpdateUserForm, UpdateProfileForm


from django.contrib.auth.models import auth

from django.contrib.auth import authenticate


from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.contrib import messages


from .models import Thought, Profile



from django.core.mail import send_mail

from django.conf import settings



# - Homepage

def home(request):

    return render(request, 'index.html')



# - Register

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            
            current_user = form.save(commit=False)
            
            form.save()            

            #send_mail("Welcome to Edenthought!", "Congratulations, on creating your account!", 
            #settings.DEFAULT_FROM_EMAIL, [current_user.email])

            # - Create a blank object for a single instance with a FK attached

            profile = Profile.objects.create(user=current_user)



            messages.success(request, "Your account was created!") 


            return redirect('my-login')


    context = {'form':form}

    return render(request, 'register.html', context=context)



# - Login

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)


        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)


            if user is not None:

                auth.login(request, user)


                messages.success(request, "Login success!")


                return redirect('dashboard')


    context = {'form':form}

    return render(request, 'my-login.html', context=context)




# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    profile_pic = Profile.objects.get(user=request.user)

    context = {'profilePic':profile_pic}


    return render(request, 'profile/dashboard.html', context=context)



@login_required(login_url='my-login')
def post_thought(request):

    form = ThoughtPostForm()

    if request.method == 'POST':

        form = ThoughtPostForm(request.POST)

        if form.is_valid():
            
            
            thought = form.save(commit=False)

            thought.user = request.user

            thought.save()


            messages.success(request, "You just posted a new thought!")


            return redirect('my-thoughts')


        
    context = {'form':form}

    return render(request, 'profile/post-thought.html', context=context)



@login_required(login_url='my-login')
def my_thoughts(request):

    user_id = request.user.id


    my_thought = Thought.objects.all().filter(user=user_id)


    context = {'thought': my_thought}


    return render(request, 'profile/my-thoughts.html', context=context)



@login_required(login_url='my-login')
def update_thought(request, pk):

    thought = Thought.objects.get(id=pk)


    form = ThoughtUpdateForm(instance=thought)


    if request.method == 'POST':

        form = ThoughtUpdateForm(request.POST, instance=thought)

        if form.is_valid():

            form.save()


            messages.success(request, "You just updated your thought!")

            return redirect('my-thoughts')


    context = {'form':form}

    return render(request, 'profile/update-thought.html', context=context)



@login_required(login_url='my-login')
def delete_thought(request, pk):

    thought = Thought.objects.get(id=pk)

    if request.method == 'POST':

        thought.delete()


        messages.success(request, "You just deleted your thought!")

        return redirect('my-thoughts')


    return render(request, 'profile/delete-thought.html')



@login_required(login_url='my-login')
def profile_management(request):

    form = UpdateUserForm(instance=request.user)   


    profile = Profile.objects.get(user=request.user)


    # - Profile form for profile picture

    form_2 = UpdateProfileForm(instance=profile)


    if request.method == 'POST':

        form = UpdateUserForm(request.POST, instance=request.user)

        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():

            form.save()

            messages.success(request, "Update - username/email was a success!")

            return redirect('dashboard')


        if form_2.is_valid():

            form_2.save()

            messages.success(request, "Your profile picture was successfully updated!")

            return redirect('dashboard')

        

    context = {'form':form, 'form_2':form_2}

    return render(request, 'profile/profile-management.html', context=context)



@login_required(login_url='my-login')
def delete_account(request):

    if request.method == 'POST':

        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        messages.success(request, "Your account was deleted successfully!")

        return redirect('my-login')


    return render(request, 'profile/delete-account.html')



# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")




















