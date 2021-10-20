from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from accounts.views import SignUpView



urlpatterns = [
path('admin/', admin.site.urls),
path('', include('crm.urls')),
path('accounts/', include('django.contrib.auth.urls')),
path('', TemplateView.as_view(template_name='home.html'), name='home'),
path('accounts/signup/', SignUpView.as_view(), name='sign_up_page'),

]




