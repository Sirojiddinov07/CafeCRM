from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import WaiterService
from .serializer import WaiterSerializer, WaiterRegisterSerializer, WaiterLoginSerializer


class WaiterListCreateView(APIView):
    permission_classes = [permissions.IsAdminUser]
    """Handles listing and creating waiters."""

    def get(self, request):
        waiters = WaiterService.list_waiters()
        serializer = WaiterSerializer(waiters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WaiterSerializer(data=request.data)
        if serializer.is_valid():
            waiter = WaiterService.create_waiter(**serializer.validated_data)
            return Response(WaiterSerializer(waiter).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WaiterDetailView(APIView):
    permission_classes = [permissions.IsAdminUser]

    """Handles retrieving, updating, and deleting a single waiter."""

    def get(self, request, waiter_id):
        waiter = WaiterService.get_waiter(waiter_id)
        return Response(WaiterSerializer(waiter).data, status=status.HTTP_200_OK)

    def put(self, request, waiter_id):
        waiter = WaiterService.update_waiter(waiter_id, **request.data)
        return Response(WaiterSerializer(waiter).data, status=status.HTTP_200_OK)

    def delete(self, request, waiter_id):
        WaiterService.delete_waiter(waiter_id)
        return Response({"message": "Waiter deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class WaiterRegisterView(APIView):
    """Handles waiter registration."""

    def post(self, request):
        serializer = WaiterRegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                waiter = WaiterService.register_waiter(**serializer.validated_data)
                return Response({"message": "Registration successful", "username": waiter.username}, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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