from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols

# Create your models here.

class Post(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    title = models.CharField(max_length=50, unique=True, 
                             error_messages={'unique' : '이미 있는 제목이네요!'})
    content = models.TextField(validators=
                               [MinLengthValidator(10, '너무 짧군요! 10자 이상 적어주세요.'),
                                validate_symbols]) # 길이에 대한 제한이 없는 문자열 필드
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    # 알아보기 쉽게 별명을 붙여준 것
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now=True)
    # auto_now_add => 데이터가 생성될 때, auto_now => 데이터가 수정될 때의 시간 저장

    def __str__(self):
        return self.title