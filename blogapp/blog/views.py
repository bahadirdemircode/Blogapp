from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category, Homework
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HomeworkForm

@login_required
def homework_create(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST, request.FILES)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.student = request.user
            homework.save()
            return redirect('homework_list')  # Gösterim sayfasına yönlendir
    else:
        form = HomeworkForm()
    return render(request, 'blog/homework_create.html', {'form': form})

@login_required
def homework_list(request):
    if request.user.is_staff:
        # Adminler tüm ödevleri görebilir
        homeworks = Homework.objects.all().order_by('-created_at')
    else:
        # Öğrenciler sadece kendi ödevlerini görebilir
        homeworks = Homework.objects.filter(student=request.user).order_by('-created_at')
    
    return render(request, 'blog/homework_list.html', {'homeworks': homeworks})

@login_required
def homework_edit(request, id):
    homework = Homework.objects.get(id=id, student=request.user)  # sadece kendi ödevini düzenleyebilir
    if request.method == 'POST':
        form = HomeworkForm(request.POST, request.FILES, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('homework_list')
    else:
        form = HomeworkForm(instance=homework)
    return render(request, 'blog/homework_create.html', {'form': form})

@login_required
def homework_delete(request, id):
    homework = Homework.objects.get(id=id, student=request.user)
    if request.method == 'POST':
        homework.delete()
        return redirect('homework_list')
    return render(request, 'blog/homework_confirm_delete.html', {'homework': homework})

@login_required
def homework_detail(request, id):
    if request.user.is_staff:
        homework = get_object_or_404(Homework, id=id)
    else:
        homework = get_object_or_404(Homework, id=id, student=request.user)

    return render(request, 'blog/homework_detail.html', {'homework': homework})




# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {
        "blog": blog
    })
    
#def blogs_by_category(request, slug):
#    context = {
#        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
#        #"blogs": Blog.objects.filter(is_active=True, category__slug=slug),
#        "categories": Category.objects.all(),
#        "selected_category": slug
#    }
#    return render(request, "blog/blogs.html", context)

def blogs_by_category(request, slug):
    category = Category.objects.get(slug=slug)  # Seçili kategoriyi al
    
    context = {
        "blogs": category.blog_set.filter(is_active=True),  # Seçili kategorinin aktif bloglarını al
        "categories": Category.objects.all(),  # Tüm kategorileri al
        "selected_category": category  # Seçili kategoriyi tam nesne olarak gönder
    }
    
    return render(request, "blog/blogs.html", context)



