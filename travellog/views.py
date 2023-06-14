from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Logentry, Country, Image
from .forms import LogentryForm, ImageForm


class LogentryList(generic.ListView):
    """
    Displays all objects of the Logentry model that are set by the user
    as 'published' and 'public'
    """
    model = Logentry
    queryset = Logentry.objects.filter(status=1, privacy=1).order_by('-year')
    template_name = 'index.html'
    paginate_by = 6


class LogentryDetail(View):
    """
    Class Based View for displaying the Details of the Logentry selected
    """

    def get(self, request, slug, *arg, **kwargs):
        queryset = Logentry.objects.all()
        logentry = get_object_or_404(queryset, slug=slug)
        images = logentry.images.all()

        return render(
            request,
            "logentry_detail.html",
            {
                "logentry": logentry,
                "images": images,
                "image_form": ImageForm()
            },
        )

    def post(self, request, slug, *arg, **kwargs):
        queryset = Logentry.objects.all()
        logentry = get_object_or_404(queryset, slug=slug)
        images = logentry.images.all()

        image_form = ImageForm(request.POST, request.FILES)

        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.logentry = logentry
            image.save()
        else:
            image_form = ImageForm()

        return render(
            request,
            "logentry_detail.html",
            {
                "logentry": logentry,
                "images": images,
                "image_form": ImageForm()
            },
        )


class AddLogentry(SuccessMessageMixin, CreateView):
    """
    Allows authenticated users to add
    and save a log entry
    """
    model = Logentry
    form_class = LogentryForm
    template_name = 'add_logentry.html'
    success_url = reverse_lazy('user_logentry')
    success_message = 'Trip Log was created successfully!'

    # Source: https://stackoverflow.com/questions/67366138/django-display-message-after-creating-a-post # noqa
    def form_valid(self, form):
        form.instance.author = self.request.user
        # msg = "Your trip log was submitted successfully"
        # messages.add_message(self.request, messages.SUCCESS, msg)
        return super(CreateView, self).form_valid(form)


class UpdateLogentry(SuccessMessageMixin, UpdateView):
    """
    Allows an authenticated user to update an already submitted Log Entry
    """
    model = Logentry
    form_class = LogentryForm
    template_name = 'update_logentry.html'
    success_url = reverse_lazy('user_logentry')
    success_message = 'Your trip log was updated successfully!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        # msg = "Your trip log was updated successfully"
        # messages.add_message(self.request, messages.SUCCESS, msg)
        return super(UpdateView, self).form_valid(form)


class DeleteLogentry(SuccessMessageMixin, DeleteView):
    """
    This allows an authenticated user to delete a log entry
    """
    model = Logentry
    template_name = 'delete_logentry.html'
    success_url = reverse_lazy('user_logentry')
    success_message = 'Your trip log was deleted successfully!'

    def delete(self, request, *args, **kwargs):
        # msg = "Your Log Entry has been deleted"
        # messages.add_message(self.request, messages.SUCCESS, msg)
        return super(DeleteView, self).delete(request, *args, **kwargs)


class UserLogentryList(generic.ListView):
    """
    Displays all objects of the Logentry model submitted only by the
    currently authenticates user, including draft and private entries.
    """
    model = Logentry
    queryset = Logentry.objects.order_by('-year')
    template_name = 'user_logentry.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = Logentry.objects.filter(
            author__id=self.request.user.id).order_by('-year')
        return queryset
