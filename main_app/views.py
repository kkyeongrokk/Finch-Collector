from django.shortcuts import render

# Create your views here.
finch = [
    {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
    {'name': 'Sachi', 'breed': 'calico',
        'description': 'gentle and loving', 'age': 2},
]


def about(request):
    return render(request, 'about.html')


def finch_index(request):
    return render(request, 'finches/index.html', {
        'finches': finch
    })
