from django.urls import path

from .views import Create_Pizza, EditOrDelete_Pizza, Filter_Pizza, Pizza_Info


urlpatterns = [
    path("info/", Pizza_Info.as_view(), name="pInfo"),
    path("create/", Create_Pizza.as_view(), name="pCreate"),
    path("editdel/", EditOrDelete_Pizza.as_view(), name="pEditDel"),
    path("filter/", Filter_Pizza.as_view(), name="pFilter")
]