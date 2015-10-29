from django.conf.urls import patterns, url

urlpatterns = [
    url(r'accueil', 'blog.views.home'),
    url(r'end', 'blog.views.end'),
    url(r'date', 'blog.views.date'),
    url(r'^add/(\d+)/(\d+)$', 'blog.views.add'),
    url(r'game', 'blog.views.game'),
]
