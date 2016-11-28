import random
import string
import hashlib

from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.shortcuts import render, render_to_response
from django.core.cache import cache

from django.template import loader

def detail_basic(request):
    """
    Return basic html which product info is written directly in html
    """
    return render_to_response(
        "content/detail_basic.html",
    )


def detail_ajax(request):
    """
    Product detail page is sent by ajax req
    """
    return render_to_response(
        "content/detail_ajax.html",
    )

def ajaxdetail(request):
    response = JsonResponse(
        {
            "title": "MAMA Jersey Top",
            "price": "$ 12.99",
        }
    )
    return response



def detail_json(request):
    return render_to_response(
        "content/detail_json.html",
    )



def detail_header(request):
    return render_to_response(
        "content/detail_header.html",
    )

def ajaxdetail_header(request):
    if not request.is_ajax():
        return HttpResponseForbidden()

    response = JsonResponse(
        {
            "title": "MAMA Jersey Top",
            "price": "$ 12.99",
        }
    )
    return response


def detail_cookie(request):
    # http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    N = 10
    token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
    cache.set(token, True, 30)
    template = loader.get_template('content/detail_cookie.html')
    resp = HttpResponse(template.render({}, request))
    resp.set_cookie("token", token, max_age=30)
    return resp

def ajaxdetail_cookie(request):
    if not request.is_ajax():
        return HttpResponseForbidden()

    cookies = request.COOKIES
    if "token" not in cookies:
        return HttpResponseForbidden()
    if not request.GET.get("token", ""):
        return HttpResponseForbidden()
    if request.GET.get("token", "") != cookies["token"]:
        return HttpResponseForbidden()

    if not cache.get(cookies["token"]):
        return HttpResponseForbidden()

    response = JsonResponse(
        {
            "title": "Congratulations",
            "price": "$ 20.00",
        }
    )
    return response


def detail_sign(request):
    # http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
    N = 10
    token = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
    cache.set(token, True, 30)
    template = loader.get_template('content/detail_sign.html')
    resp = HttpResponse(template.render({}, request))
    resp.set_cookie("token", token, max_age=30)
    return resp

def ajaxdetail_sign(request):
    if not request.is_ajax():
        return HttpResponseForbidden()

    cookies = request.COOKIES
    if "token" not in cookies:
        return HttpResponseForbidden()
    if not request.GET.get("sign", ""):
        return HttpResponseForbidden()

    m = hashlib.md5()
    m.update(cookies["token"])
    sign = m.hexdigest()

    if request.GET.get("sign") != sign:
        return HttpResponseForbidden()

    if not cache.get(cookies["token"]):
        return HttpResponseForbidden()

    response = JsonResponse(
        {
            "title": "Congratulations",
            "price": "$ 20.00",
        }
    )
    return response






















