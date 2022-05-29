from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json
from .models import Cursor, Data_wo_to_en
import random


def api(request):
    """
    with open('data.json', 'r') as fp:
        dataframe = fp.read()
        dataframe = json.loads(dataframe)

    for i in range(1, 14024):
        data = Cursor(value=i)
        data.save()
        """
    cursor = random.randrange(1, 14000)
    wolof = Data_wo_to_en.objects.get(id=cursor)
    wolof = wolof.wolof

    return JsonResponse({'new_sentence': wolof, 'cursor': cursor})


def apitranslate(request, translate, cursor):
    # cursor = Cursor.objects.all()
    # cursor = int(cursor[0].value)
    wolof = Data_wo_to_en.objects.get(id=cursor+1)
    wolof.english = translate
    wolof.is_translate = True
    wolof.save()
    deleted_cursor = Cursor.objects.get(value=cursor+1)
    deleted_cursor.delete()

    return JsonResponse({'is_translate': True})


def apichange(request, cursor):
    cursor = cursor + 1
    wolof = Data_wo_to_en.objects.get(id=cursor+1)
    wolof_txt = wolof.wolof
    print(Data_wo_to_en.objects.get(id=cursor+2).is_translate)
    while Data_wo_to_en.objects.get(id=cursor+2).is_translate:
        cursor = cursor + 2
        wolof = Data_wo_to_en.objects.get(id=cursor)
        wolof_txt = wolof.wolof

    data_to_send = {'new_sentence': wolof_txt, 'cursor': cursor}
    return JsonResponse(data_to_send)
