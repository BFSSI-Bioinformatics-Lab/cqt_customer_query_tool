from django.urls import path, re_path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.QueryView.as_view(), name='home_page'),
    path('user/<str:username>', views.UserListView.as_view(), name='user_list'),
    path('query/<int:pk>/', views.QueryDetailView.as_view(), name='query_detail'),
#     path('entry/new/', views.EntryCreateView.as_view(), name='entry_create'),
#     path('entry/<int:pk>/update/', views.EntryUpdateView.as_view(), name='entry_update'),
#     path('entry/<int:pk>/delete/', views.EntryDeleteView.as_view(), name='entry_delete'),
#     path('entry/archives/', views.EntryHistoryView.as_view(), name='entry_archives'),
#     path('entry/archives/<int:pk>/', views.HistoryDetailView.as_view(), name='history_detail'),
]