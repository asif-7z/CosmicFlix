from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from upload_video.models import video
from .serializers import videoSerializer,VideoDetailSerializer,VideoCreateSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import (IsAuthenticated)



class videoListView(ListAPIView):
    queryset = video.objects.all()
    serializer_class = videoSerializer


class VideoDetailView(RetrieveAPIView):
    queryset = video.objects.all()
    serializer_class = VideoDetailSerializer
    lookup_field = 'slug'

class VideoCreateView(CreateAPIView):
    queryset = video.objects.all()
    serializer_class = VideoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    