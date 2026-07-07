from rest_framework import serializers

from reviews.models import Comment, Review, User
from reviews.validators import validate_username


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150, validators=[validate_username]
    )
    email = serializers.EmailField(max_length=254)

    def validate(self, data):
        username = data['username']
        email = data['email']
        user_by_username = User.objects.filter(username=username).first()
        user_by_email = User.objects.filter(email=email).first()
        if user_by_username != user_by_email:
            if user_by_username is not None:
                raise serializers.ValidationError(
                    {'username': 'Этот username уже занят другим email.'}
                )
            raise serializers.ValidationError(
                {'email': 'Этот email уже используется другим username.'}
            )
        return data


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('pub_date',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('pub_date',)
