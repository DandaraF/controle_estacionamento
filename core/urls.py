from django.urls import path, include
from .views import (home, parkingview, newParking, editParking, deleteParking,
                    outParking,payParking)

urlpatterns = [
    path("", home),
    path("parking/<int:id>", parkingview, name="parking-view"),
    path("parking", newParking, name="new-parking"),
    path("parking/<int:id>/out", outParking, name="out-parking"),
    path("parking/<int:id>/pay", payParking, name="pay-parking"),
    # path("parking/<str:plate>", historicParking, name="pay-parking"),
    path("edit/<int:id>", editParking, name="edit-parking"),
    path("delete/<int:id>", deleteParking, name="delete-parking"),

    # path("salvar/", salvar, name="salvar"),
    # path("update/<int:id>", update, name="update"),
    # path("delete/<int:id>", delete, name="delete")
]
