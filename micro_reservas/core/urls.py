from django.urls import path
from .views import courtsAllViewSet, registerusers, loginView, courtsfull, tutorial_list, tutorial_detail, partners_serializerall, partners_serializer, courtsfull_detail

urlpatterns = [
    path('api/list_all_courts', courtsAllViewSet.as_view()),
    path('api/register_user', registerusers.as_view()),
    path('api/login_user', loginView.as_view()),
    path('api/courtsfull', courtsfull.as_view()),
    path('api/tutorial', tutorial_list),
    path('api/tutoriales/<pk>', tutorial_detail),
    path('api/partners', partners_serializerall),
    path('api/partners/<pk>', partners_serializer),
    # todo enpoints para crud de courts
    #path('api/courtsfull', courtsfull),
    path('api/courtsfull/<pk>', courtsfull_detail)
]
