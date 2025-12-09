from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from shorts.models import Short, ShortClick


def redirect_short(_, code):
    short = get_object_or_404(Short, code=code)
    if short.is_expired or short.private:
        raise Http404
    ShortClick.objects.create(short=short)
    return redirect(short.target)
