from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView

from leaderboard_app.models import Heroes
from leaderboard_site.settings import BASE_DIR1


class LeaderView(ListView):
    model = Heroes
    template_name = 'leaderboard_app/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LeaderView, self).get_context_data(**kwargs)
        obj = Heroes.objects.all()
        context['heroes_many'] = []
        for i in obj:
            index = (i.apples + i.level + i.health + i.moneys) / 4
            context['heroes_many'].append((i.name, i.apples, i.level, i.health, i.moneys, index, i.inventory, i.weapon))
        sorted(context['heroes_many'], key=lambda key: key[5])
        print(context['heroes_many'])
        return context


def test_func_please(request):
    print(BASE_DIR1)
    return HttpResponse('Бац')
