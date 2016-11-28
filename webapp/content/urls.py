#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016-11-02 michael_yin
#

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail_basic$', views.detail_basic, name='detail_basic'),

    url(r'^detail_ajax$', views.detail_ajax, name='detail_ajax'),
    url(r'^ajaxdetail$', views.ajaxdetail, name='ajaxdetail'),

    url(r'^detail_json$', views.detail_json, name='detail_json'),

    url(r'^detail_header$', views.detail_header, name='detail_header'),
    url(r'^ajaxdetail_header$', views.ajaxdetail_header, name='ajaxdetail_header'),

    url(r'^detail_cookie$', views.detail_cookie, name='detail_cookie'),
    url(r'^ajaxdetail_cookie$', views.ajaxdetail_cookie, name='ajaxdetail_cookie'),

    url(r'^detail_sign$', views.detail_sign, name='detail_sign'),
    url(r'^ajaxdetail_sign$', views.ajaxdetail_sign, name='ajaxdetail_sign'),
]
