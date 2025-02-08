from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import WaiterService
from .serializer import WaiterLoginSerializer



class WaiterLoginView(APIView):
    """Handles waiter login using session authentication."""

    def post(self, request):
        serializer = WaiterLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                waiter = WaiterService.login_waiter(request, **serializer.validated_data)
                return Response({"message": "Login successful", "username": waiter.username}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WaiterLogoutView(APIView):
    """Handles waiter logout."""

    def post(self, request):
        WaiterService.logout_waiter(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)