from django.urls import path, include
urlpatterns = [
    path(",index,name="index")
    path("menu/",include("game.urls.menu.index")),
    path("palyground/",include("game.urls.playground.index")),
    path("settings/",include("game.urls.settings.index")),
]

