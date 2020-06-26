from django.shortcuts import render


def noter_list(request):
    return render(request, 'noterler/noter_list.html', {})
