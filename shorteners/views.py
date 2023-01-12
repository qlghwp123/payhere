from django.shortcuts import redirect
import random, string
from django.utils import timezone
from datetime import timedelta
from .models import Link
from django.http import JsonResponse


def shortener(request):
    slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
    short = request.path + slug

    link = Link.objects.create(
        # link : https://stackoverflow.com/questions/27325505/how-to-get-the-previous-url-from-a-post-in-django
        origin=request.META['HTTP_REFERER'],
        new=short,
        expire=timezone.now() + timedelta(hours=3)
    )

    link.save()

    return JsonResponse({'link': link.new})


def original(request, new):
    short = "/s/" + new
    link = Link.objects.get(new=short)

    if timezone.now() < link.expire:
        return redirect(link.origin)
    else:
        return redirect('accounts:login')