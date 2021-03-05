import json

import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from sklearn import preprocessing


def index(request):
    path = "Neural_Module\\" + str("1") + ".txt"
    names = ["T", "F7", "F3", "F4", "F8", "T3", "C3", "Cz", "C4", "T5", "P3", "Pz", "P4", "T6", "O1", "O2"]
    data = pd.read_csv(path, sep=" ", names=names, header=0, skiprows=2)

    N_DATA = 500
    NUMBER_CHANNELS = 16
    mas = np.zeros((N_DATA,NUMBER_CHANNELS))

    for i in range(1, NUMBER_CHANNELS):
        mmax = abs(max(data[0:N_DATA][names[i]]))
        mmin = abs(min(data[0:N_DATA][names[i]]))
        allMax = max(mmax, mmin)

        for j in range(N_DATA):
            mas[j][i] = (5*i + (data[0:N_DATA][names[i]][j]) / allMax)  # для нормального отображение графиков сделаем нормировку
    mas[:, 0] = data[0:N_DATA][names[0]]


    df = pd.DataFrame(data=mas, columns=names)
    # result = data.to_json(orient="columns")
    # parsed = json.loads("{\"data\":" + result + "}")
    # json1 = json.dumps(parsed, indent=4)

    result = df.to_json(orient="records")
    parsed = json.loads(result)
    json.dumps(parsed, indent=4)

    d = [
        {'x': 0, 'y1': 2},
        {'x': 1, 'y1': 8},
        {'x': 2, 'y1': 10},
        {'x': 6, 'y1': 3},
    ]

    return HttpResponse(json.dumps(parsed, indent=4))


@csrf_exempt
def index2(request):
    if request.method == "POST":
        d = {'dict': 1, 'dictionary': 2}
        return HttpResponse(json.dumps(d))

    return HttpResponse("Hello World. First Django Project. PythonCircle.Com")
