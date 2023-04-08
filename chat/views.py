from django.shortcuts import redirect, render
from HomeModule.models import userProfile
from django.http import HttpResponse,JsonResponse
from chat.models import Message,Room
# Create your views here.


def room(request,postkey):
    if userProfile.objects.filter(key = postkey).exists():
        receiverprofile = userProfile.objects.get(key = postkey)
        receiverKey = receiverprofile.key
        senderprofile = userProfile.objects.get(profile_username = request.user)
        senderKey = senderprofile.key
        username = request.user
        roomkey = receiverKey+senderKey
        revcheck = senderKey+receiverKey
        if Room.objects.filter(name = roomkey).exists():
            context = {'username':username,'roomkey':roomkey,'userkey':senderKey}
            return render(request,'room.html',context)
        elif Room.objects.filter(name=revcheck).exists():
            context = {'username':username,'roomkey':revcheck,'userkey':senderKey}
            return render(request,'room.html',context)
        else:
            new_room = Room.objects.create(name=roomkey,senderkey=senderKey,receiverkey=receiverKey)
            new_room.save()
            context = {'username':username,'roomkey':roomkey,'userkey':senderKey}
            return render(request,'room.html',context)
        
        
    else:
        return redirect('/')




def sendmessage(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    roomkey = request.POST.get('roomkey')
    userkey = request.POST.get('userkey')
    print(message)
    new_message = Message.objects.create(value=message, user = username, room = roomkey,userkey = userkey)
    new_message.save()
    print("Message saved")
    return HttpResponse("Message sent successfully")


def getMessages(request,roomkey):
    messages = Message.objects.filter(room = roomkey)
    print(messages)
    return JsonResponse({"messages":list(messages.values())})


