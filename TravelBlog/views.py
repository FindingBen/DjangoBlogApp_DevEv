from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )

from .models import Journey



def home(request):
    context = {

        'journeys': Journey.objects.all()

    }

    return render(request, 'home.html',context)

def dashboard(request):
    context = {

        'journeys': Journey.objects.all()

    }

    return render(request, 'dashboard.html',context)


class JourneyListView(ListView):
    model = Journey
    template_name = 'home.html'
    context_object_name = 'journeys'
    ordering = ['-date_posted']


class JourneyDetailView(DetailView):
    model = Journey
    template_name = 'journey_detail.html'

class JourneyCreateView(LoginRequiredMixin, CreateView):
    model = Journey
    template_name = 'journey_form.html'
    fields = ['title', 'description','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def journey_image_upload(request):
    #     if request.method == 'POST':
    #         form = Journeyform(request.POST, request.FILES)
    #         if form.is_valid():
    #             form.save()
    #             img_obj = form.instance
                

class JourneyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Journey
    template_name = 'journey_form.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        journey = self.get_object()
        if self.request.user == journey.author:
            return True
        return False

class JourneyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Journey
    template_name = 'confirm_delete_journey.html'
    success_url = '/'
    def test_func(self):
        journey = self.get_object()
        if self.request.user == journey.author:
            return True
        return False



