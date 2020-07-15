from django.shortcuts import render
from django.http import HttpResponse
tasks = [
    {
        'author': 'Rambabu',
        'task_title': 'Complete Django Series',
        'is_checked': 0,
        'date_posted': 'January 19th, 2020'
    },
    {
        'author': 'CoreyMS',
        'task_title': 'Complete CP',
        'is_checked': 1,
        'date_posted': 'May 25th, 2018'
    },
    {
        'author': 'CoreyMS',
        'task_title': 'Participate in Codechef July Long Challenge',
        'is_checked': 1,
        'date_posted': 'May 25th, 2018'
    },
    {
        'author': 'Rambabu',
        'task_title': 'Participate in Codeforces Challenges',
        'is_checked': 0,
        'date_posted': 'May 25th, 2018'
    }

]


def home(request):
    context = {
        'tasks': tasks
    }
    return render(request, 'to_do_app/home.html', context)

def test(request):
    return render(request, 'to_do_app/test.html')
