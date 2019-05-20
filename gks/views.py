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
    choice_criteria = [int(i) for i in request.GET.getlist('criteria')]
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
        all_standard.append(lb.standard(lb.create_diagram(matrix, i), choice_criteria))

    ans, all_compromise = lb.create_r(matrix, choice_criteria)
    standard_plan = lb.full_bout(matrix)[ans]
    standard_diagram = lb.create_diagram(matrix, standard_plan)
    del standard_diagram[0]

    for i in range(len(all_standard)):
        all_standard[i].append(all_compromise[i])
        all_standard[i].insert(0, lb.full_bout(matrix)[i])

    context = {
        'matrix': matrix,
        'johnson_plan': johnson_plan,
        'johnson_diagram': johnson_diagram,
        'criteria': all_standard,
        'criteria_diagram': standard_diagram,
        'criteria_plan': standard_plan,
        'length': range(36),
        'choice_criteria': choice_criteria,
        'all_compromise': all_compromise,
        'name': lb.full_bout(matrix)
    }
    return render(request, 'gks/result.html', context)
