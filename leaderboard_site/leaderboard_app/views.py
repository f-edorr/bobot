from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView

from leaderboard_app.models import Heroes
from leaderboard_site.settings import BASE_DIR


class LeaderView(ListView):
    model = Heroes
    template_name = 'leaderboard_app/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LeaderView, self).get_context_data(**kwargs)
        obj = Heroes.objects.all()

        for i in obj:
            index = (i.apples + i.level + i.health + i.moneys) / 4
        return context


def g(request):
    print(BASE_DIR)
    return HttpResponse('Бац')
