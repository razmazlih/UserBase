from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import User
from .serializers import (
    UserSerializer,
    CreateUserSerializer,
    ChangePasswordSerializer,
    ChangeUsernameSerializer,
)


class UserProfileView(RetrieveUpdateAPIView):
    """
    קריאה ועדכון פרופיל המשתמש.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class CreateUserView(CreateAPIView):
    """
    יצירת משתמש חדש.
    """

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class ChangePasswordView(APIView):
    """
    שינוי סיסמת המשתמש.
    """

    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data["new_password"])
            user.save()
            return Response(
                {"message": "הסיסמה שונתה בהצלחה."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeUsernameView(APIView):
    """
    שינוי שם המשתמש.
    """

    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = ChangeUsernameSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            user.username = serializer.validated_data["new_username"]
            user.save()
            return Response(
                {"message": "שם המשתמש שונה בהצלחה."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
