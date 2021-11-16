from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Category, Psychologist
from .serializers import CategorySerializer, LoginSerializer, PsychologistSerializer, RegisterSerializer


class PsychologistViewSet(viewsets.ModelViewSet):
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RequestConsultationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        psychologist = (
            Psychologist.objects.filter(status="ready", blocked=False, in_an_appointment=False)
            .values()
            .first()
        )

        if psychologist:
            return Response(data=psychologist, status=status.HTTP_200_OK)

        return Response(data={"message": "Not a Psychologist found"}, status=status.HTTP_404_NOT_FOUND)


class AcceptConsultationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, psychologist_id):
        psychologist = Psychologist.objects.filter(id=psychologist_id).first()

        if psychologist.in_an_appointment:
            return Response(
                data={"message": "Psychologist already in an appointment"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            psychologist.in_an_appointment = True
            psychologist.save()
            return Response(data={"message": "Consultation successfully accepted"}, status=status.HTTP_200_OK)


class CloseConsultationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.auth["user_id"]
        psychologist = Psychologist.objects.filter(user_id_id=user_id).first()

        if not psychologist:
            return Response(
                data={"message": "You don't have your register ended yet"}, status=status.HTTP_404_BAD_REQUEST
            )

        if psychologist.in_an_appointment:
            psychologist.in_an_appointment = False
            psychologist.save()
            return Response(data={"message": "Consultation successfully ended"}, status=status.HTTP_200_OK)
        else:
            return Response(
                data={"message": "You are not currently on an appointment."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserHasPsychologistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.auth["user_id"]
        psychologist = Psychologist.objects.filter(user_id_id=user_id).values().first()

        if psychologist:
            return Response(data=psychologist, status=status.HTTP_200_OK)

        return Response(data={"message": "Not a Psychologist found"}, status=status.HTTP_404_NOT_FOUND)
