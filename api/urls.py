from django.urls import path
from .views import CategoriesView, CategoriesGetView

urlpatterns = [
    path('categories/<id>', CategoriesGetView.as_view(), name='get_categories'),
    path('categories', CategoriesView.as_view(), name='post_categories'),

]
