from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Logentry, Country
from .forms import LogentryForm


class LogentryList(generic.ListView):
    model = Logentry
    queryset = Logentry.objects.filter(status=1).order_by('-year')
    template_name = 'index.html'
    paginate_by = 6


class LogentryDetail(View):

    def get(self, request, slug, *arg, **kwargs):
        queryset = Logentry.objects.filter(status=1)
        logentry = get_object_or_404(queryset, slug=slug)
        # images = logentry.images

        return render(
            request,
            "logentry_detail.html",
            {
                "logentry": logentry,
                # "images": images,
            },
        )


class AddLogentry(CreateView):
    """
    Allows authenticated users to add
    and save a log entry
    """
    model = Logentry
    form_class = LogentryForm
    template_name = 'add_logentry.html'
    success_url = reverse_lazy('home')

    # Source: https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post # noqa
    def form_valid(self, form):
        form.instance.author = self.request.user
        # msg = "Your trip log was submitted successfully"
        # messages.add_message(self.request, messages.SUCCESS, msg)
        return super(CreateView, self).form_valid(form)
