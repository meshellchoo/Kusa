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


from django.urls import path

from . import authentication, iSteamUserStats, iSteamUser, views, manageUser



app_name = "Kusa" 
urlpatterns = [
    path('GetGlobalAchievementPercentagesForApp/', iSteamUserStats.get_global_achievement_percentages_for_app, name='GetGlobalAchievementPercentagesForApp'),
    path('GetPlayerAchievements/', iSteamUserStats.get_player_achievements, name='GetPlayerAchievements'),
    path('GetUserStatsForGame/', iSteamUserStats.get_user_stats_for_game, name='GetUserStatsForGame'),
    path('GetPlayerSummaries/', iSteamUser.get_player_summaries, name='GetPlayerSummaries'),
    path('GetFriendList/', iSteamUser.get_friend_list, name='GetFriendList'),
    path('GetOwnedGames/', iSteamUserStats.get_owned_games, name='GetOwnedGames'),
    path('login', authentication.LoginView.as_view(), name='login'),
    path('logout', authentication.LogoutView.as_view(), name='logout'),
    path('close', views.close_view, name='close'),
    path('getToken/', authentication.get_token, name='getToken'),
    path('addEmail/', manageUser.add_email, name="addEmail"),
    path('UpdateGoal/', manageUser.adjust_goal, name='UpdateGoal'),
    path('ToggleUserEmail/', manageUser.toggle_email, name='ToggleEmail'),
    path('getAllUsers/', manageUser.get_all_users, name='get_all_users'),
    path('deleteAUser/', manageUser.delete_a_user, name='delete_a_user'),
    path('getAUser/', manageUser.steamuser_detail, name='steamuser_detail'),
    path('getPlaytime/', views.get_user_daily_hours, name='get_playtime'),
    path('Deactivate/', manageUser.deactivate_account, name='DeactivateUser'),
    path('getDailyHours/', views.get_user_daily_hours, name='get_user_daily_hours'),
    path('getAchievements/', views.get_user_achievements, name='get_user_daily_hours'),
]