from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required(login_url='login/') 
def frontpage(request):
    posts = Post.objects.all()
    return render(request, "frontpage.html", {"posts": posts})

@login_required(login_url='login/')
def post_create(request):
    next_cnt = "post" + str(Post.objects.count() + 1)
    print("post_create:" + request.method)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # new_post = form.save(commit=False)
            # new_post.save()
            title = form.cleaned_data['title']
            slug = form.cleaned_data['slug']
            job = form.cleaned_data['job']
            qualification = form.cleaned_data['qualification']
            print(qualification)
            location = form.cleaned_data['location']
            body = form.cleaned_data['body']
            price = form.cleaned_data['price']
            agent = form.cleaned_data['agent']
            create_user = request.user
            form = Post.objects.create(title=title, slug=slug, job=job, qualification=qualification, location=location, body=body, price=price, agent=agent, create_user=create_user)
            return redirect("frontpage")
    else:
        form = PostForm()
        
    return render(request, "post_create.html", {"next_cnt": next_cnt, "form": form})

@login_required(login_url='login/')
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "post_detail.html", {"post": post})

class ClientLoginView(LoginView):
    fields = "__all__"
    template_name = "login.html"
    # def post(self, request):
    #     return render(request,"login.html")
    def get_success_url(self):
        return reverse_lazy("frontpage")