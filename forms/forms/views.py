from django.shortcuts import render

def home(request):
    return render(request,'index.html')


def about(request):
    user_input=request.GET['user_input']
    return render(request,'about.html',{'about_input':user_input})
