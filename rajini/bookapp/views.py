from django.shortcuts import render

def front_cover(request):
    return render(request, 'cover/frontcover.html')
