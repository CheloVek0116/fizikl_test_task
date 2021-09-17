from base64 import b64encode

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.image.serializers import ImageSerializer
from apps.image.services.rotate import flip_image


class FlipImageView(APIView):
    serializer_class = ImageSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_image = serializer.validated_data.get('file')
        flipped_image = flip_image(file_image)
        base64_flipped_image = b64encode(flipped_image.read())
        return Response({'file': base64_flipped_image})
