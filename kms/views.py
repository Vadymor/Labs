from django.shortcuts import render
import numpy as np
from . import lab

# Create your views here.


def index(request):
    b_c, answer, alpha_js, minmax = lab.result()
    context = {
        'b_c': [i.tolist() for i in b_c],
        'answer': answer,
        'alpha_js': alpha_js,
        'minmax': minmax
    }
    return render(request, 'kms/index.html', context)
