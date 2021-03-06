"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .loan import views as loanviews
from .contracts import views as contractsviews

router = routers.DefaultRouter()
router.register(r'users', loanviews.UserViewSet)
router.register(r'groups', loanviews.GroupViewSet)

router.register(r'contracts', contractsviews.ContractViewSet)
router.register(r'payments', contractsviews.PaymentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]