
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["POST"])
def sample_report(request):
    try:
        return Response("hello world", status=status.HTTP_200_OK)
    except ValueError as e:
        return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)