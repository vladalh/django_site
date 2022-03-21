from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def index(request):
    return render(request, 'basic/index.html')


def about_us(request):
    return render(request, 'basic/about_us.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Некорректное заполнение формы'
    form = ReviewForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'basic/create.html', context)


def comments_all(request):
    reviews = Review.objects.order_by('-id')
    return render(request, 'basic/comments_all.html', {'title': 'Отзывы', 'reviews': reviews})
