from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post

# Create your views here.
def home(request):
    post = Post.objects.all()

    return render (request, "index.html", {'p': post })


def details(request, id):
    post = Post.objects.get( pk=id)
    return render (request, "details.html", {'p': post })


def postdel(request, id ):
    post = Post.objects.get( pk=id)
    if request.method == "POST":
        pas = request.POST['passw']
        if post.password == pas:
            post.delete()
            messages.success(request, 'Your post is successfully deleted')
            return redirect('home' )
        else:
            messages.error(request, 'Type password correctly')
            return redirect('home')

        

    
    return render (request, "delete.html", {'pi': id })



def handlepost(request):
    if request.method == "POST":
        password= request.POST['password']
        rname= request.POST['rname']
        dishname= request.POST['dname']
        description= request.POST['dtext']
        price= request.POST['price']
        # dateTime= request.POST['dateTime']
        imag = request.FILES.get('file')

        post = Post(password =password, reasturantName= rname, dishName=dishname,description= description, price=price,  image=imag)
        post.save()
        messages.success(request, 'Your post is successfully posted')
        return redirect('home' )
    else:
        return  HttpResponse("bal kha")





def handlelogin(request):
    return render (request, "login.html")






def handlelogout(request):
    logout(request)
    messages.success(request, 'You are successfully logout')
    return redirect('home' )


def post(request):
    return render (request, "post.html")
    


def send(request):
    if request.method == "POST":
        username= request.POST['uname']
        password= request.POST['passw']

        user = authenticate( username=username, password = password)
        
        if user is not None:
            login( request, user)
            return redirect('home')
        else:
            messages.error(request, 'Please login correctly')
            return redirect('login')



    else:
        return  HttpResponse("bal kha")



def createUser(request):
    if request.method == "POST":
        username = request.POST['rname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if len(username) > 20  or password!= password2  or len(password) < 4  :
            messages.error(request, 'Please fill the form correctly')
            return redirect('home')
            
        if not username.isalnum() :
            messages.error(request, 'Please fill the form correctly')
            return redirect('home')


        # if not username.isalnum():
        #     return redirect('home')
        
        # if password!= password2:
        #     return redirect('home')
        else:
            user = User.objects.create_user( username, email, password2)
            user.save()
            messages.success(request, 'Your account has been successfuly sent, please login to post')
            return redirect('home')
        




    else:
        return HttpResponse("hahahahhah")