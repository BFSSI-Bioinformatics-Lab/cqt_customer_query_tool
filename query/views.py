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
from . import forms

# Create your views here.

class QueryView(LoginRequiredMixin, ListView):
    model = Query
    template_name = 'Query/home_page.html'
    context_object_name = 'queries'
    # paginate_by = 2
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

class QueryCreateView(LoginRequiredMixin, CreateView):
    model = Query
    template_name = 'Query/query_form.html'
    context_object_name = 'query'
    form_class = forms.QueryForm
    # fields = '__all__'

    # set author in form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# logging required, but also,
# For only author can update entries add "UserPassesTestMixin" plus uncomment
class QueryUpdateView(LoginRequiredMixin, UpdateView):
    model = Query
    template_name = 'Query/update_query_form.html'
    context_object_name = 'query'
    form_class = forms.UpdateQueryForm
    # fields = '__all__'

    # set author in form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # # Func to test if author is the one updating
    # def test_func(self):
    #     # get query
    #     item = self.get_object()
    #     if self.request.user == item.author:
    #         return True
    #     return False
    
class QueryDeleteView(LoginRequiredMixin,  DeleteView):
    model = Query
    template_name = 'Query/query_confirm_delete.html'
    context_object_name = 'query'
    success_url = '/' # sent to home after deleting

    # # Func to test if author is the one updating
    # def test_func(self):
    #     # get query
    #     item = self.get_object()
    #     if self.request.user == item.author:
    #         return True
    #     return False
    
class QueryHistoryView(LoginRequiredMixin, ListView):
    template_name = "Query/query_history_list.html"

    def get_queryset(self):
        history = Query.history.all()
        return history


class HistoryDetailView(LoginRequiredMixin, DetailView):
    model = Query.history.model
    template_name = 'Query/history_detail.html'
    context_object_name = 'history'