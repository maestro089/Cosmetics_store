from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('store.urls')),
    path('moderator/', include('moderator.urls')),
    path('news/', include('news.urls')),
    path('cart/', include('cart.urls')),
    path('account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
