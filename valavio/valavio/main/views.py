from django.shortcuts import render
from django.views import generic as views
# Create your views here.
from valavio.common.view_mixins import RedirectToDashboard


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'main/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True#  за да не ни се показват допълнителните полета, проверката е в base.html
        return context

    '''def dispatch()  е в common/view_mixins.py, RedirectToDashboard го наследява от там'''
    pass




