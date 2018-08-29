from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.core import serializers

from .models import Record, RecordFields
from .forms import RecordForm


# Create your views here.
def detail(request, record_id):

    record = get_object_or_404(Record, pk=record_id)
    
    # fields = RecordFields.objects.filter(record=record)

    print(record.fields)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecordForm(request.POST, instance=record)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()

            return redirect('repo:index')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecordForm(instance=record)

    return render(request, 'repo/detail.html', {'form': form, 'id': record_id})

    # context = {
    #     'record': record,
    #     'fields': fields,
    # }
    #
    # if request.method == 'POST':
    #
    #     record.name = request.POST['name']
    #     record.fields = request.POST["fields"]
    #     record.save()
    #
    # return render(request, 'repo/detail.html', context)


def index(request):
    model = Record.objects.all()

    context = {
        'model': model,
    }
    return render(request, 'repo/index.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class Records(View):

    def get(self, request):
        results = Record.objects.all().values()

        return JsonResponse(list(results), safe=False)

    # def delete(self, request):
    #     data = json.loads(request.body)
    #     pk = data.get('pk')
    #     Project.objects.get(pk=pk).delete()
    #     response = json.dumps({'status': 'ok'})
    #     return HttpResponse(response, content_type="application/json")
    #
    # def post(self, request):
    #     data = json.loads(request.body)
    #     form = ProjectForm(data)
    #     if form.is_valid():
    #         new_project = form.save()
    #         response = serializers.serialize("json", [new_project])
    #     else:
    #         response = json.dumps({'errors': form.errors})
    #     return HttpResponse(response, content_type="application/json")
