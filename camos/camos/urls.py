from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from camos_app.views import home, frontpage, post_detail, post_create, ClientLoginView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('offer/', frontpage, name="frontpage"),
    path('post_create/', post_create, name="post_create"),
    path('login/', ClientLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path("<slug:slug>/", post_detail, name="post_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)