from django.urls import path
from restapi.views import ItemPG,ItemGUD
urlpatterns = [
    path('pg/',ItemPG.as_view()),
    path('gud/<uuid:id>',ItemGUD.as_view()),
]
