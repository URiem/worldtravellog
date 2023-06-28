from django.shortcuts import render

# https: // levelup.gitconnected.com/django-customize-404-error-page-72c6b6277317


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
