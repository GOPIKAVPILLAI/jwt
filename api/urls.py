from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from core.views import Register,Login

urlpatterns = [
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',Register.as_view()),
    path('login/',Login.as_view())
]
