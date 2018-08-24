from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Record, RecordFields


# Create your views here.
def detail(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    model = RecordFields.objects.filter(record=record)

    context = {
        'model': model,
    }
    return render(request, 'repo/detail.html', context)


def index(request):
    model = Record.objects.all()

    context = {
        'model': model,
    }
    return render(request, 'repo/index.html', context)
