from django.contrib import admin
from cards.models import Card
# Register your models here.
@admin.register(Card)
class PersonAdmin(admin.ModelAdmin):
    list_display=('question','answer')
