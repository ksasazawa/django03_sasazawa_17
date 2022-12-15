from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from camos_app.views import home, frontpage, provider_frontpage, provider_map, post_detail, post_create, ClientLoginView, ProviderLoginView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('offer/', frontpage, name="frontpage"),
    path('provider/', provider_frontpage, name="provider_frontpage"),
    path('provider_map/', provider_map, name="provider_map"),
    path('post_create/', post_create, name="post_create"),
    path('clientlogin/', ClientLoginView.as_view(), name="clientlogin"),
    path('providerlogin/', ProviderLoginView.as_view(), name="providerlogin"),
    path('logout/', LogoutView.as_view(next_page="/"), name="logout"),
    path("<slug:slug>/", post_detail, name="post_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)