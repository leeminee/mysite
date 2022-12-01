from django.apps import AppConfig

# mysite/settings.py 파일에 INSTALLED_APPS 설정에 아래와 같이 들어가야 한다.
# polls.apps.PollsConfig

class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
