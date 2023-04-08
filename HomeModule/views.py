import random
from sqlite3 import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from HomeModule.models import Post, userProfile
from chat.models import Room

# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    allProfiles = userProfile.objects.all()
    roomcount = 0

    if request.user.is_authenticated:
        userprofile = userProfile.objects.get(profile_username=request.user)
        userkey = userprofile.key
        roomcount = len(Room.objects.filter(senderkey=userkey) | Room.objects.filter( receiverkey = userkey)) 
    context = {'allPosts':allPosts,'allProfiles':allProfiles,'roomcount':roomcount}
    return render(request,'home.html', context)

def profile(request):
    totalposts = len(Post.objects.filter(author = request.user))
    userprofile = userProfile.objects.get(profile_username=request.user)
    userkey = userprofile.key
    roomcount = len(Room.objects.filter(senderkey=userkey) | Room.objects.filter( receiverkey = userkey)) 
    userstatus = userprofile.status
    if request.method == "POST":
        print(request.POST.get('status'))
        userprofile.status = request.POST.get('status')
        userprofile.save()
        return redirect('/profile')

    
    
  
    context = {'totalposts':totalposts,'roomcount':roomcount,'userstatus':userstatus,'userkey':userkey}
    return render(request, 'profile.html',context)

def fav(request):
    allrooms = Room.objects.all()
    allprofiles = userProfile.objects.all()
    userprofile = userProfile.objects.get(profile_username=request.user)
    userkey = userprofile.key
    userprofile = userProfile.objects.get(profile_username=request.user)
    userkey = userprofile.key
    userstatus = userprofile.status

    roomcount = len(Room.objects.filter(senderkey=userkey) | Room.objects.filter( receiverkey = userkey)) 
    context = {'allrooms':allrooms,'userkey':userkey,'roomcount':roomcount,'userstatus':userstatus,'allprofiles':allprofiles}
    return render(request,'fav.html',context)

def dump(request):
    if request.method == "POST":
        postkey = 0
        author = request.user
        body = request.POST['content-area']
        allProfiles = userProfile.objects.all()
        for profile in allProfiles:
            print(profile.profile_username, author)
            if str(profile.profile_username) == str(author):
                postkey = profile.key
                break
        newpost = Post(author=author,body = body,postkey = postkey)
        newpost.save()
        print("New post has been added successfully!")
        userprofile = userProfile.objects.get(profile_username=request.user)
        userkey = userprofile.key
        roomcount = len(Room.objects.filter(senderkey=userkey) | Room.objects.filter( receiverkey = userkey)) 
        return render(request,"dump.html",{'roomcount':roomcount})
    userprofile = userProfile.objects.get(profile_username=request.user)
    userkey = userprofile.key
    roomcount = len(Room.objects.filter(senderkey=userkey) | Room.objects.filter( receiverkey = userkey)) 
    return render(request,"dump.html",{'roomcount':roomcount})


# Login/Signup Modules
#----------------------------------------------------------------------------------
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    return render(request,'login.html')


def handlelogout(request):
    logout(request)
    return redirect('/')

#-----------------------------------------------------------------------------------


#For Unique Username verification
#----------------------------------------------------------------------------
def checkUniqueUsername(username):
    if User.objects.filter(username = username).first():
        return False
    return True

def uniqueKey(key):
    allProfiles = userProfile.objects.all()
    for profile in allProfiles:
        if profile.key!=key:
            return True
        else:
            return False


def signup(request):
 
    if request.method == "POST":
        username = request.POST['username']
        if checkUniqueUsername(username):

            password = request.POST['password']
            email = request.POST['email']
            
                
            #Registering new user
            user = User.objects.create_user(username = username, password=password, email=email)
            user.save()
            key = random.randint(111,999)
            if uniqueKey(key):
                userprofile = userProfile()
                userprofile.profile_username = username
                userprofile.key = key
                userprofile.save()
            else:
                key = random.randint(1111,9999)
                userprofile = userProfile()
                userprofile.profile_username = username
                userprofile.key = key
                userprofile.save()

            print("User is successfully registered!")
            return render(request,'signup.html')
        
        else:
            print("User not registered!")
            flag = True
            context = {'flag':flag}
            return render(request,'signup.html',context)

    return render(request,'signup.html')

#----------------------------------------------------------------------------------------------------------