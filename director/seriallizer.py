from rest_framework import serializers

from . import models


def validate_name_min_length(value, min_length):
    if len(value) < min_length:
        raise serializers.ValidationError(f'минимальная длина для этого поля должна быть {min_length}')
    return value


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = 'id name movies_count'.split()

    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, obj):
        return obj.movies.count()

    def validate_name(self, value):
        validate_name_min_length(value, 5)
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

    def validate_text(self, value):
        validate_name_min_length(value, 5)
        return value


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = models.Movie
        fields = '__all__'

    def get_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

    def validate_title(self, value):
        validate_name_min_length(value, 5)
        return value
