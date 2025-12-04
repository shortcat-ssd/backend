from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from shorts.models import Short, ShortView

import secrets

CODE_LENGTH = 8


def generate_code():
    while True:
        code = secrets.token_urlsafe(CODE_LENGTH)[:CODE_LENGTH]
        if not Short.objects.filter(code=code).exists():
            return code


def redirect_short(request, code):
    short = get_object_or_404(Short, code=code)
    if short.is_expired:
        raise Http404
    if short.private and (
        not request.user.is_authenticated or request.user != short.user
    ):
        raise Http404
    ShortView.objects.create(short=short)
    return redirect(short.target)
