from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .movies_service import MoviesService
from django.core.cache import cache

class MovieListView(APIView):

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('ghiblikey', openapi.IN_QUERY, description="Your Ghibli Key", type=openapi.TYPE_STRING,  required=True),
        openapi.Parameter('format', openapi.IN_QUERY, description="Format of the Response", type=openapi.TYPE_STRING),
    ])
    def get(self, request):
        ghiblikey_value = request.query_params.get('ghiblikey')
        is_api_request = request.query_params.get('format') == 'json'

        if ghiblikey_value == "ghiblivalue":
            movies_actors_list = cache.get('movies_actors_list')
            if not movies_actors_list:
                movies_actors_list = MoviesService().get_movies_actors()
                cache.set('movies_actors_list', movies_actors_list, 60)

            if is_api_request:
                return Response({'movies_actors_list': movies_actors_list})
            else:
                context = {'movies_actors_list': movies_actors_list}
                return render(request, "movies/index.html", context)

        if is_api_request:
            return Response({'error': 'Invalid API key'}, status=403)
        else:
            return render(request, "movies/error.html", {'error_message': 'Invalid API key'})
