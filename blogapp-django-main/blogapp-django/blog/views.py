from django.shortcuts import render,Http404,get_object_or_404
from .models import Post
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.views.generic.edit import CreateView



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def contact(request):
    return render(request, 'blog/contact.html')
def about(request):
    return render(request, 'blog/about.html')
def index(request):
  object_list=Post.objects.all()
  context={'object_list':object_list}
  return render(request,'blog/home.html',context)

def detail(request,blog_id):
  blog=get_object_or_404(Post,pk=blog_id)
  return render(request,'blog/detail.html',{'blog':blog})


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/add.html'
    fields = ['title', 'body', 'author', 'image'] 
class BlogUpdateView(UpdateView):
  model=Post
  template_name='blog/edit.html'
  fields=['title','body']

class BlogDeleteView(DeleteView):
  model=Post
  template_name='blog/delete.html'
  success_url=reverse_lazy('blog:index')
  
  
