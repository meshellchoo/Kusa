"""admin URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import iSteamUserStats, iSteamUser, views, manageUser,friendList

from rest_framework import routers
from Kusa import views

# router = routers.DefaultRouter()
# router.register(r'todos',views.FriendsListView,'todo')

# router = routers.DefaultRouter()
# router.register('TestInfo', views.TestView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('test', views.test, name='test'),
    path('GetGlobalAchievementPercentagesForApp/', iSteamUserStats.get_global_achievement_percentages_for_app, name='GetGlobalAchievementPercentagesForApp'),
    path('GetPlayerAchievements/', iSteamUserStats.get_player_achievements, name='GetPlayerAchievements'),
    path('GetUserStatsForGame/', iSteamUserStats.get_user_stats_for_game, name='GetUserStatsForGame'),
    path('GetPlayerSummaries/', iSteamUser.get_player_summaries, name='GetPlayerSummaries'),
    path('GetOwnedGames/', views.get_owned_games, name='GetOwnedGames'),
    #path('RegisterUser/', manageUser.register_user, name='RegisterUser')


    path('add_post/', friendList.add_post),
    path('update_post/<str:receiver_steamid>&<str:request_steamid>', friendList.update_friendRequest),
    #path('delete_post/<str:id>', views.delete_post),
    path('friendRequest/<str:receiver_name>&<str:sender_name>',friendList.friendRequest),
    path('read_post_all/',views.read_post_all),
    path('getFriendList/<str:userName>', friendList.getFriendList),
    path('getFriendRequest/<str:userName>', friendList.getFriendRequest),

    #path('update_post/<str:receiver_steamid>', friendList.update_friendRequest),
    
    
    
]