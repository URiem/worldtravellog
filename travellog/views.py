from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Logentry


class LogentryList(generic.ListView):
    model = Logentry
    queryset = Logentry.objects.filter(status=1).order_by('-year')
    template_name = 'index.html'
    paginate_by = 6


class LogentryDetail(View):

    def get(self, request, slug, *arg, **kwargs):
        queryset = Logentry.objects.filter(status=1)
        logentry = get_object_or_404(queryset, slug=slug)
        images = logentry.images

        return render(
            request,
            "logentry_detail.html",
            {
                "logentry": logentry,
                # "images": images,
            },
        )
