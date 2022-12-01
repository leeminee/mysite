
from django.contrib import admin
from django.urls import include, path

# 여기는 최상위 URLconf 이다.
# polls.urls 모듈을 바라보게 설정하기위해 include 함수를 사용하였다.

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
