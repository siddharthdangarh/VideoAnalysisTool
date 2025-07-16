import json
import logging
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from search.models import VideoFile
from search.search_engine.index import VideoSearchEngine

logger = logging.getLogger(__name__)


class SearchView(APIView):

    def get(self, request):
        try:
            return render(request, 'search/index.html')
        except Exception as e:
            logger.exception(e)
            return render(request, 'error.html')

    def post(self, request):
        try:
            data = request.data
            query = data.get("query")
            if not query:
                return JsonResponse({"error": "No query provided"}, status=400)

            video_file_id = data.get("video_file_id")
            if not video_file_id:
                return JsonResponse({"error": "No video file id provided"}, status=400)

            video_file = VideoFile.objects.get(video_file_id=video_file_id)
            chunks = video_file.chunks

            search_engine = VideoSearchEngine(chunks)
            
            result = search_engine.search(query, top_k=1)[0]
            if not result:
                return JsonResponse({"error": "No result found"}, status=400)

            return JsonResponse({
                "video": result["video_id"],
                "timestamp": f"{int(result['start'])}s",
                "text": result["text"]
            })
        except Exception as e:
            logger.exception(e)
            return JsonResponse({"error": True, "message": "Something went wrong"}, status=500)
