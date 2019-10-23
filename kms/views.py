from django.shortcuts import render
import numpy as np
from . import lab

# Create your views here.


def index(request):
    b_c, answer, alpha_js, minmax, max_w = lab.result()
    # np.random.randn()
    context = {
        'b_c': [i.tolist() for i in b_c],
        'answer': answer,
        'alpha_js': alpha_js,
        'minmax': minmax,
        'max_w': max_w
    }
    return render(request, 'kms/index.html', context)
