"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include  #路徑簡潔命名功能
from django.contrib import admin  #內建app管理
from django.contrib.auth import views as auth_views 
from app import views #對應app的views 呼叫回應網頁
urlpatterns = [
    url(r'^admin/', admin.site.urls), #後台管理
    # url(r'^', include('app.urls')),
    # url(r'^accounts/login',auth_views.login),
    # url(r'^accounts/logout', veiws.logout), 
    # url(r'^coffee/$', views.coffee), #內頁
    url(r'^$', views.front_page), #沒輸入網指登入首頁
    url(r'^front_page/$', views.front_page), # 首頁查詢 → 物件清單 ; 首頁查詢 → 人才招募
    url(r'^spartan/$', views.spartan), # 人才招募
    url(r'^select_page/$', views.select_page), # 物件清單 → 物件內容
    url(r'^result_page/$', views.result_page), # 物件內容 
    url(r'^visualize_page/$', views.visualize_page),
    url(r'^error_page/$', views.error_page), 
    url(r'^add_my_love/$', views.add_my_love,name='ajax-dict'),
    url(r'^ajax_dict/$', views.ajax_dict,name='ajax-dict'),
    # url(r'^area_result_page/$', views.area_result_page),
     
]
