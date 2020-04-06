from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from . forms import UserRegisterForm
from .models import BoardModel,ProfileModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            # return render(request, 'login.html', {'some':100})
            return redirect('login')
            # return redirect('register')
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            try:
                name= ProfileModel.objects.get(author=username2)
            except:
                return redirect('register')
            
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required
# def listfunc(request):
#     object_list = BoardModel.objects.all()
#     profile_img = ProfileModel.objects.all()
    
#     return render(request, 'list.html', {'object_list':object_list,'profile_img': profile_img})

def logoutfunc(request):
    logout(request)
    return redirect('login')

    
def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.goodmember:
        return redirect('list')
    else:
        post.good += 1
        post.goodmember = post.goodmember + ' ' + post2
        post.save()
        return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')

class UserRegisterView(CreateView):
    print("Here1")
    template_name = 'register.html'
    model = ProfileModel
    fields = ('url_code', 'author', 'icon', 'introduce')
    print("Here2")
    success_url = reverse_lazy('list')

class PostEdit(UpdateView):
    template_name = 'postedit.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('profile')

class ProfileEdit(UpdateView):
    template_name = 'profileedit.html'
    model = ProfileModel
    fields = ('url_code', 'author', 'icon', 'introduce')
    success_url = reverse_lazy('profile')

class BoardDelete(DeleteView):
    template_name = 'delete.html'
    model = BoardModel
    success_url = reverse_lazy('profile')

class TopicList(ListView):
    template_name = 'list.html'
    model = BoardModel
    # context_object_name = 'object_list' 
    def get_queryset(self):
        return BoardModel.objects.order_by('-created_at')
    
    


# class ProfileView(ListView):
#     template_name = 'myprofile.html'
#     context_object_name = 'topic_list'

#     def get_queryset(self):
#         return ProfileModel.objects.filter(url_code = self.kwargs['url_code'])

def myprofilefunc(request):
    name= ProfileModel.objects.get(author=request.user)
    pk=name.id
    username=name.author
    
    object = ProfileModel.objects.get(pk=pk)
    print('AAAAAAAAAAAA')
    post_all =BoardModel.objects.filter(author = username).order_by('-created_at')
    return render(request, 'myprofile.html', {'object':object,'post_all':post_all})
     
    
def profilefunc(request, pk):
    
    getdata = BoardModel.objects.get(id=pk)
    username =getdata.author
    pk2= ProfileModel.objects.get(author=username)
    pk =pk2.id
    print('AAAAAAAAAAAA')
    object = ProfileModel.objects.get(pk=pk)
    post_all =BoardModel.objects.filter(author = username).order_by('-created_at')


    return render(request, 'allprofile.html', {'object':object,'post_all':post_all})