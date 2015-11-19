from django.shortcuts import render, HttpResponse
from random import sample, choice


def home(request):
    return render(request, 'hrsk/home.html', {})


def generate_new_hrsk(request):
    horoskop = update_horoskop()
    return HttpResponse(horoskop)


def update_horoskop():
    list_of_first = ['Es könnte sein, dass ',
    'Sei nicht überrascht, wenn ',
    'Es ist gut möglich, dass ',
    'Die Sterne sagen, dass ', 
    'Sei darauf gefasstc',
    'Erwarte reinen Herzens ' 
]

    list_of_second = ['wenn die Götter Dir gewogen sind',
    'beim nächsten Vollmond',
    'wenn Hase und Igel nachts auf einer Sandbank Schlittschuh laufen',
    'im nächsten Monat ',
    'diese Woche ',
    'am Mittwoch ',
    'im Zoo ',
    'auf dem Heimweg ',
    'durch eine übernatürliche Erscheinung ',
    'heute ', 
    'wenn der Hahn dreimal kräht'
    'wenn Medusa hustet'
    'wenn eine Katze deinen Weg kreuzt',
    'wenn Du guten Mutes bist']


    list_of_third = ['etwas wunderbares passiert.',
    'ein interessanter Mensch in dein Leben tritt.',
    'eine gute Gelegenheit auf dich wartet.',
    'Kekse auf dich herab regnen.',
    'ein Pappnasenclown dein Herz erobert.',
    'ein Papagei dich Eierkopf nennt.',
    'Du die Liebe deines Lebens triffst.'
    'Du ein Glück findest, nach dem Du nicht gesucht hast.']

    first = sample(list_of_first, 1)
    second = sample(list_of_second, 1)
    third = sample(list_of_third, 1)

    horoskop = choice(first) + choice(second) + choice(third)
    return horoskop
    print(horoskop)

