from django.shortcuts import render
import numpy as np
from . import lab_3_gks as lb

# Create your views here.


def index(request):
    return render(request, 'gks/index.html', {})


def table(request):
    if request.method == "GET":
        if 'amount' in request.GET:
            context = {
                'amount': range(int(request.GET['amount'])),
                'column': range(3)
            }
            return render(request, 'gks/table.html', context)
    return render(request, 'gks/table.html', {})


def result(request):
    time_prepare = request.GET.getlist('matrix')
    length = len(time_prepare)
    time_prepare = np.asarray(time_prepare, dtype="float64").reshape(int(length/3), -1).tolist()
    matrix = {}
    for i in range(len(time_prepare)):
        matrix[i+1] = time_prepare[i]
    johnson_plan = lb.johnson(matrix)
    johnson_diagram = lb.create_diagram(matrix, lb.johnson(matrix))
    del johnson_diagram[0]

    all_standard = []
    for i in lb.full_bout(matrix):
        all_standard.append(lb.standard(lb.create_diagram(matrix, i)))

    ans, all_compromise = lb.create_r(matrix)
    standard_plan = lb.full_bout(matrix)[ans]
    standard_diagram = lb.create_diagram(matrix, standard_plan)
    del standard_diagram[0]

    context = {
        'matrix': matrix,
        'johnson_plan': johnson_plan,
        'johnson_diagram': johnson_diagram,
        'criteria': all_standard,
        'criteria_diagram': standard_diagram,
        'criteria_plan': standard_plan,
        'length': range(36)
    }
    return render(request, 'gks/result.html', context)
