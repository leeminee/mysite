from django.urls import path

from . import views

# view 를 호출 하기 위해 생성한 URLconf 파일이다.

urlpatterns = [
    path('', views.index, name='index'), # 💡 polls/views.py 의 index 함수로 간다는 뜻?
]