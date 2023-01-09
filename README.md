Bai 1: cai dat, tao project, tim hieu luong chay, url, templates
may moi tren vs
- sau khi tao foder workspace
- cai django vao python:
	pip install django
- tao mot project django:
	django-admin startproject site1
tao ra file manage.py, settings.py, urls.py.
- tao mot app cho trang web:
	python manage.py startapp home
- tao mot db
	python manage.py migrate
- chay server
	python manage.py runserver 8080

- luong chay: tu duong dan goc co url home/ se di toi home.urls, home.urls se vao ham views.index
ham views.index goi index.html trong templates.

*chu y: tao file base.html de extends, dung {%block %} {%endblock%}

Bai 2: static va toi uu url
- tao foder static/home: chua file css, js...
- trong setting thu muc goc co cau hinh STATIC_URL = 'static/'
- trong file base.html muon dung cac file static/home:
	{% load static %} : load static/
	href="{% static 'home/style.css' %}" : dung file css
- muon dung url trong the <a href="{% url 'post:home' %}">Post</a>
	post: ten app la post
	home: name='home' (app_name = 'post' path('', views.blog, name='home'))
