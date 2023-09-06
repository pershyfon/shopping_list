from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Sabrina Aviana Dewi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)