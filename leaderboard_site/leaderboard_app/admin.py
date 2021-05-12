from django.contrib import admin

# Register your models here.
from leaderboard_app.models import Heroes


@admin.register(Heroes)
class HeroesAdmin(admin.ModelAdmin):
    fields = ('user_id', 'name', 'gender', 'apples', 'moneys', 'health', 'level', 'inventory', 'weapon')
