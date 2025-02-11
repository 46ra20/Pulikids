from django.shortcuts import redirect
from rest_framework.views import APIView
from .serializers import StudentRegistrationSerializers,TeacherRegistrationSerializers,UserLoginSerializer
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

class StudentRegistrationView(APIView):
    serializer_class = StudentRegistrationSerializers

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response('Registration complete successfully.')
        return Response('Sorry, Enter validate data to complete your registration')

class TeacherRegistrationView(APIView):
    serializer_class = TeacherRegistrationSerializers

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response('Registration complete successfully.')
        return Response('Sorry, Enter validate data to complete your registration')
    

class LoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request,username=username,password=password)
            print(user)

            getUser = login(request=request, user=user, backend='django.contrib.auth.backends.ModelBackend')
            print(getUser)

            if user:
                token,_ = Token.objects.get_or_create(user=user)
                return Response({'token':str(token),'user_id':user.id})
            else:
                return Response({"error":"Invalid credentials"})
        else:
            return Response(serializer.errors)
        
class LogoutView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')

 