from django.urls import path
# url - 주소(정규표현식으로 주소를 표현), 뷰
# path - 주소(기존 정규표현식을 간단히 표현할 수 있게 컨버터), 뷰
# re_path - 주소(정규표현식으로 주소를 표현), 뷰

# 뷰는 함수형, 클래스형 두 종류로 만들 수 있다.
# 결국은 장고에서는 모든 뷰는 함수형으로 동자하게 되어있다.

from .views import *

urlpatterns = [
    # 함수형 뷰 : 함수이름
    # 클래스형 뷰 : 클래스이름.as_view()
    # href="{% url 'bookmark_create' %}"
    # naver.com/blog/update/?doc_id=1234
    # naver.com/blog/update/1234/
    # r"update/(?P<pk>\d+)/"
    path("delete/<int:pk>/", BookmarkDelete.as_view(), name='bookmark_delete'),
    path("update/<int:pk>/",BookmarkUpdate.as_view(), name='bookmark_update'),
    path("write/", BookmarkCreate.as_view(), name='bookmark_create'),
    path("", BookmarkList.as_view(), name='bookmark_list'),
]