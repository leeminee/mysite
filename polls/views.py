from venv import logger

from django.http import HttpResponse

def index(request):
    logger.info('request : ', request) # 💡 왜 이 로그가 안찍히지?
    return HttpResponse("Hello, world. You're at the polls index.")
