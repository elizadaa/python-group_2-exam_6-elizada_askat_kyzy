"""exam_6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from webapp.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, UserInfoDetailView, UserInfoListView,UserInfoUpdateView

app_name = 'webapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('users', UserInfoListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserInfoDetailView.as_view(), name='user_detail'),
    path('users/update/<int:pk>', UserInfoUpdateView.as_view(), name='user_update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)