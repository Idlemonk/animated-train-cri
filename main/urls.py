from . import views
from django.contrib import admin
from django.urls import path, include, re_path
from . views import home, submit_recovery_request, track_status, about, wallet_recovery, blockchain_explorer, crypto_converter, contact_view, news_updates, write_up
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', home, name='home'),
        path('submit_request/', submit_recovery_request, name='submit_request'),
        path('track_status/', track_status, name='track_status'),
        path('about/', about, name='about'),
        path('wallet_recovery/', wallet_recovery, name='wallet_recovery'),
        path('blockchain_explorer/', blockchain_explorer, name='blockchain_explorer'),
        path('crypto_converter/', crypto_converter, name='crypto_converter'),
        path('contact/', contact_view, name='contact'),
        path('news_updates/', news_updates, name= 'news_updates'),
        path('write-up/', write_up, name= 'write_up'),
        
        
        
        
]
# Removed invalid line
if settings.DEBUG:       
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

