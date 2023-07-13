from django.urls import path, re_path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.QueryView.as_view(), name='home_page'),
    path('user/<str:username>', views.UserListView.as_view(), name='user_list'),
    path('query/<int:pk>/', views.QueryDetailView.as_view(), name='query_detail'),
    path('query/new/', views.QueryCreateView.as_view(), name='query_create'),
    path('query/<int:pk>/update/', views.QueryUpdateView.as_view(), name='query_update'),
    path('query/<int:pk>/delete/', views.QueryDeleteView.as_view(), name='query_delete'),
    path('query/archives/', views.QueryHistoryView.as_view(), name='query_archives'),
    path('query/archives/<int:pk>/', views.HistoryDetailView.as_view(), name='history_detail'),
    path('query/download/', views.QueryDownloadView.as_view(), name='query_download'),
]