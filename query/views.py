from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from api.models import Query
from cqt_customer_query_tool.users.models import User
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# Create your views here.

class QueryView(LoginRequiredMixin, ListView):
    model = Query
    template_name = 'Query/home_page.html'
    context_object_name = 'queries'
    # paginate_by = 10
#     order entries from newest to oldest
    ordering = ['-updated']

class UserListView(LoginRequiredMixin, ListView):
    model = Query
    template_name = 'Query/user_query.html'
    context_object_name = 'queries'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Query.objects.filter(evaluator=user).order_by('-updated')

class QueryDetailView(LoginRequiredMixin, DetailView):
    model = Query
    template_name = 'Query/detail_page.html'
    context_object_name = 'query'
