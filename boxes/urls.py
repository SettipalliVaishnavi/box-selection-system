from django.urls import path

from . import views

urlpatterns = [
    path("recommend-box/", views.recommend_from_payload, name="recommend-box"),
    path("orders/<str:reference>/recommend-box/", views.recommend_for_existing_order,
         name="order-recommend-box"),
]
