from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import seriallizer, models


@api_view(['GET'])
def director_list_view(request):
    directors = models.Director.objects.all()
    data = seriallizer.DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director_id = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status=404, data={'message': 'Director not found'})
    data = seriallizer.DirectorSerializer(director_id).data
    return Response(data=data)


@api_view(['GET'])
def movie_list_view(request):
    movies = models.Movie.objects.all()
    data = seriallizer.MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie_id = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status=404, data={'message': 'Movie'})
    data = seriallizer.MovieSerializer(movie_id).data
    return Response(data=data)


@api_view(['GET'])
def review_list_view(request):
    reviews = models.Review.objects.get(id=id)
    data = seriallizer.ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review_id = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=404, data={'message': 'Review'})
    data = seriallizer.ReviewSerializer(review_id).data
    return Response(data=data)


@api_view(['GET'])
def test(request):
    context = {
        'integer': 100,
        'string': 'hello world',
        'boolean': True,
        'list': [
            1, 2, 3
        ]
    }
    return Response(data=context)
