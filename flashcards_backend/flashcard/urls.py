from django.urls import path
from flashcard import views

urlpatterns = [
    path('allcollections/', views.get_all_collections),
    path('addcollection/', views.add_collection),
    path('deletecollection/<int:collection_id>/', views.delete_collection),
    path('editcollection/<int:collection_id>/', views.update_collection),
]