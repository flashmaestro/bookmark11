from django.shortcuts import render

# Create your views here.
# CRUDL
# 미리 만들어져있는 자주 사용하는 형태의 뷰 -> 제네릭 뷰

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Bookmark

# def bookmarkList(request):
#     object_list = Bookmark.objects.all()
#     return render(request,"bookmark/bookmark_list.html", {'object_list':object_list})

class BookmarkList(ListView):
    # 제네릭 뷰를 사용한다.
    # 1. 필요한 제네릭 뷰를 상속받는다.
    # 2. 사용할 모델을 설정한다.
    model = Bookmark
    # 앱/모델명_list.html을 렌더링하겠다.
    # 앱/모델명_form.html
    # 앱/모델명_detail.html
    # 앱/모델명_confirm_delete.html

    # 만약 뷰에서 출력해야할 모델 데이터가 있다면!
    # 단일 객체를 보여줘야 하는 경우 : object
    # 복수 객체를 보여줘야 하는 경우 : object_list

from django.urls import reverse_lazy

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name','url','description']
    success_url = reverse_lazy('bookmark_list')

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['description']
    success_url = reverse_lazy('bookmark_list')

class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark_list')
    #template_name_suffix = "_delete"
    template_name = 'bookmark/bookmark_delete.html'
