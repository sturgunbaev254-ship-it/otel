from django.urls import path,include
from .views import login,logout,registor,HotelsViewSet,NumbersViewSet,BookingViewSet,ReviewsViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r"hotels",HotelsViewSet),
router.register(r"numbers",NumbersViewSet),
router.register(r"booking",BookingViewSet),
router.register(r"reviews",ReviewsViewSet),


urlpatterns=[
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('registor/',registor,name='registor'),
    
    path("",include(router.urls)),
    
]