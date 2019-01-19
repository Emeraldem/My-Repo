from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Video, Comment


def hello(request):
    names = ["Egor", "Petr", "Fedor", "Elena"]
    return render(request, "video.html", {"content": names})
    return HttpResponse("<h1>hello</h1>")

def showall(request):
    videos = Video.objects.all()
    content = []#[(video,[(com,user),(),(),(),...]),(),(),(),.....]
    for vid in videos:
        list_com = []
        comments = Comment.objects.filter(Comment_Video_id = vid.id)
        for com in comments:
            user = User.objects.get(id = com.Comment_User_id)
            list_com.append((com, user))
        content.append((vid, list_com))
    return render(request, "video.html", {"content":content})



def showone(request, video_id):
    video = Video.objects.get(id = video_id)
    comment = Comment.objects.filter(Comment_Video_id=video_id)
    users = []
    for com in comment:
        user = User.objects.get(id=com.Comment_User_id)
        users.append(user)
    return render(request, "showone.html", {"video":video,
                                            "comment":comment,
                                            "users":users})



# Create your views here.
