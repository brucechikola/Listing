from django.urls import path, include
from .views import API_Login, LoggedInUserView, UserList, FriendsView, UserFriendsView, AddNewFriend, Unfriend, Delete
urlpatterns = [
    path('', API_Login),
    path(r'/login', API_Login),
    path('/users', UserList.as_view()),
    path('/user-friends/<str:pk>', UserFriendsView),
    path(r'/user', LoggedInUserView.as_view()),
    path(r'/friends', FriendsView.as_view()),
    path(r'/add-new-friend', AddNewFriend),
    path(r'/unfriend', Unfriend),
    path(r'/delete/<str:pk>', Delete)
]