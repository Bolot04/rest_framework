from django.contrib import admin
from django.urls import path, include

from director import views
from director.views import DirectorListAPIView, MovieListAPIView, MovieDetailAPIView, ReviewListAPIView, \
    ReviewDetailAPIView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/directors/', views.director_list_api_view),
#     path('api/v1/director/<int:id>/', views.director_detail_api_view),
#     path('api/v1/movies/', views.movie_list_api_view),
#     path('api/v1/movie/<int:id>', views.movie_detail_api_view),
#     path('api/v1/reviews/', views.review_list_api_view),
#     path('api/v1/review/<int:id>', views.review_detail_api_view),
#     path('', include('users.urls')),
# ]
urlpatterns = [
    path('categories/', DirectorListAPIView.as_view()),
    path('products/categories/<int:pk>/', DirectorListAPIView.as_view()),
    path('products/', MovieListAPIView.as_view()),
    path('products/<int:pk>/', MovieDetailAPIView.as_view()),
    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('', include('users.urls')),
]
