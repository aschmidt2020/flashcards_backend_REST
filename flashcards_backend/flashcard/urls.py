from django.urls import path
from flashcard import views

urlpatterns = [
    path('allcollections/', views.get_all_collections),
    path('addcollection/', views.add_collection),
    path('deletecollection/<int:collection_id>/', views.delete_collection),
    path('editcollection/<int:collection_id>/', views.update_collection),
    path('allflashcards/<int:collection_id>/', views.get_all_flashcards),
    path('addflashcard/<int:collection_id>/', views.add_flashcard),
    path('deleteflashcard/collection/<int:collection_id>/flashcard/<int:flashcard_id>/', views.delete_flashcard),
    path('editflashcard/collection/<int:collection_id>/flashcard/<int:flashcard_id>/', views.update_flashcard),
]