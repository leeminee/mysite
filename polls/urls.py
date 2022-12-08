from django.urls import path

from . import views

# view 를 호출 하기 위해 생성한 URLconf 파일이다.

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'), # 💡 polls/views.py 의 index 함수로 간다는 뜻?
    # ex: /polls/5/
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='result'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

