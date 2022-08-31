from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, DirectorDetailSerializer, MovieSerializer, MovieDetailSerializer, ReviewSerializer, ReviewDetailSerializer


# @api_view(['GET'])
# def test_view(request):
#     dict_ = {
#         'text': 'hello',
#         'int': 100,
#         'float': 9.99,
#         "booleon": True,
#         "list": [
#             1, 2, 3
#         ],
#        'dict': {'new': 'yes'}
#     }
#     return Response(data=dict_)

@api_view(['GET', 'POST'])
def Directors(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    else:
        name = request.date.get('name')
        Director.objects.create(name=name)
        return Response(data={'message': 'create'})

@api_view(['GET', 'PUT', 'DELETE'])
def Directors_detail(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=404)
    if request.method == 'GET':
        serializer = DirectorDetailSerializer(directors)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        directors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        directors.name = request.data.get('name')
        return Response(data={'message': 'update'})

@api_view(['GET', 'POST'])
def Movies(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    else:
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        category_id = request.data.get('category_id')
        Movie.objects.create(title=title, description=description, duration=duration, category_id=category_id)
        return Response(data={'message': 'created'})

@api_view(['GET', 'PUT', 'DELETE'])
def Movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'movie not found'},
                        status=404)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.category_id = request.data.get('category_id')
        return Response(data={'message': 'update'})


@api_view(['GET', 'POST'])
def Reviews(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    else:
        text = request.data.get('text')
        star = request.data.get('star')
        catagory_id = request.data.get('category_id')
        Review.objects.create(text=text, star=star, catagory_id=catagory_id)
        return Response(data={'message': 'create'})

@api_view(['GET', 'PUT', 'DELETE'])
def Review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found'},
                        status=404)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        review.text = request.data.get('text')
        review.star = request.data.get('star')
        review.catagory_id = request.data.get('category_id')
        return Response(data={'message': 'update'})

@api_view(['GET'])
def MovieReview(request):
    mov = Movie.objects.all()
    data = MovieSerializer(mov, many=True).data
    return Response(data=data)
