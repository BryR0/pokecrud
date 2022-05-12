from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import ApiCreateForm
from .models import Api
from django.urls import reverse_lazy
import time


# Create your views here.

class ApiListView(View):
    def get(self, request, *args, **kwargs):
        api = Api.objects.all()
        context = {
            'apis': api
        }

        return render(request, 'api_list.html', context)


class ApiCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ApiCreateForm()
        context = {
            'form': form
        }
        return render(request, 'api_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = ApiCreateForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES['file']

                name = form.cleaned_data.get('name')
                p, created = Api.objects.get_or_create(name=name, image=file)
                p.save()
                return redirect('api:home')
            else:
                form = ApiCreateForm()
                # return render(request, 'upload.html', {'form': form})

                context = {
                }
                return render(request, 'api_create.html', context)


class ApiDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        api = get_object_or_404(Api, pk=pk)
        context = {
            'api': api
        }
        return render(request, 'api_detail.html', context)


class ApiUpdateView(UpdateView):
    model = Api
    fields = ['name', 'image']
    template_name = 'api_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('api:detail', kwargs={'pk': pk})


class ApiDeleteView(DeleteView):
    """
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

    def get(self, *args, **kwargs):
        """
    model = Api
    template_name = 'api_delete.html'
    success_url = reverse_lazy('api:home')
