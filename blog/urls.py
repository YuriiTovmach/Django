from django.conf.urls import url, include
from blog import views



urlpatterns = [
    url(r'^blog/$', views.blog, name='blog'),

    # url(r'^$', views.BlogListView, name='home'),
    # url(r'post/<int:pk>/', views.BlogDetailView, name='post_detail'),
]


