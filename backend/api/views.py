from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserDashboardSerializer
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_description="Get API root with available endpoints",
    responses={
        200: openapi.Response(
            description="List of available endpoints",
            examples={
                "application/json": {
                    "signup": "/api/signup/",
                    "login": "/api/login/",
                    "dashboard": "/api/dashboard/",
                    "logout": "/api/logout/",
                    "schema": "/api/schema/"
                }
            }
        )
    }
)
@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    """
    API Root endpoint.
    
    Available endpoints:
    - POST /api/signup/ - Register a new user
    - POST /api/login/ - Login and get JWT tokens
    - GET /api/dashboard/ - Get user dashboard data (requires authentication)
    - POST /api/logout/ - Logout and invalidate token
    """
    return Response({
        'signup': '/api/signup/',
        'login': '/api/login/',
        'dashboard': '/api/dashboard/',
        'logout': '/api/logout/',
        'schema': '/api/schema/'
    })

@swagger_auto_schema(
    method='post',
    operation_description="Register a new user",
    request_body=UserRegistrationSerializer,
    responses={
        201: openapi.Response(
            description="User created successfully",
            schema=UserRegistrationSerializer
        ),
        400: "Bad Request - Invalid data"
    }
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    """
    Register a new user.
    
    Required fields:
    - first_name: string
    - last_name: string
    - email: string (unique)
    - password: string
    - password2: string (must match password)
    - role: string ('SUPER ADMIN' or 'ADMIN')
    """
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserDashboardSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    operation_description="Login user",
    request_body=UserLoginSerializer,
    responses={
        200: openapi.Response(
            description="Login successful",
            schema=UserLoginSerializer
        ),
        401: "Unauthorized - Invalid credentials",
        400: "Bad Request - Invalid data"
    }
)
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Login user.
    
    Required fields:
    - email: string
    - password: string
    """
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserDashboardSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    operation_description="Logout user",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token to blacklist')
        },
        required=['refresh']
    ),
    responses={
        200: "Logout successful",
        400: "Bad Request - Invalid token"
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    """
    Logout user and blacklist refresh token.
    
    Required fields:
    - refresh: string (refresh token to blacklist)
    """
    try:
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successfully logged out'})
        except Exception as e:
            # If token is invalid or already blacklisted, still return success
            return Response({'message': 'Successfully logged out'})
    except Exception as e:
        return Response({'message': 'Successfully logged out'})

@swagger_auto_schema(
    method='get',
    operation_description="Get dashboard data",
    responses={
        200: openapi.Response(
            description="Dashboard data retrieved successfully",
            schema=UserDashboardSerializer
        ),
        401: "Unauthorized - Invalid or missing token"
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    """
    Get dashboard data for authenticated user.
    """
    return Response({
        'user': UserDashboardSerializer(request.user).data,
        'widgets': {
            'total_users': 100,
            'active_users': 75,
            'pending_tasks': 5,
            'completed_tasks': 25
        }
    })
