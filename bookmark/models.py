from django.db import models

# Create your models here.
# 모델은 어떤 데이터를 어떤 형식으로 어떤 제약조건을 가지고 DB에 저장할 것인지?
# + 사용자에게 입력받을 때 어떤 형식으로 어떤 제약조건을 가지고 입력받을 것인가?
# 1. ORM 기능을 사용하기 위해서 Model클래스를 상속받는다.
# 2. 원하는 데이터가 있다면 필드로 작성
class Bookmark(models.Model):
    site_name = models.CharField(max_length=30, verbose_name="사이트명")
    url = models.URLField(verbose_name="주소")
    description = models.TextField(blank=True,verbose_name="설명")

    def __str__(self):
        return self.site_name + " : " + self.url

    class Meta:
        ordering = ['site_name']

    # 모델 작성을 끝낸 후
    # $ python manage.py makemigrations
    # $ python manage.py sqlmigrate bookmark 0001
    # $ python manage.py migrate