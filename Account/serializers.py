from rest_framework import serializers
from .models import TeacherRegistrationModel,StudentRegistrationModel
from django.contrib.auth.models import User

ACCOUNT_TYPE = [
    ('STUDENT','Student'),
    ('TEACHER','Teacher'),
]

class StudentRegistrationSerializers(serializers.ModelSerializer):
    image = serializers.ImageField()
    confirm_password=serializers.CharField(required = True)
    department = serializers.CharField()
    student_id=serializers.CharField()
    section = serializers.CharField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password','image','department','student_id','section']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        account_type = 'STUDENT'
        image = self.validated_data['image']
        department = self.validated_data['department']
        student_id=self.validated_data['student_id']
        section = self.validated_data['section']


        print(username,first_name,last_name,email,password,confirm_password,account_type,image)

        if password!=confirm_password:
            raise serializers.ValidationError({'error':"password didn't match"})
        # if password != '/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/':
        #     raise serializers.ValidationError({'error':'Please enter a strong password'})
        
        if User.objects.filter(email=email):
            raise serializers.ValidationError({'error':"Email already exist"})

        account = User(username=username,first_name=first_name,last_name=last_name,email=email)
        user_model = StudentRegistrationModel(user=account,account_type=account_type,image=image,department=department,student_id=student_id,section=section)
        account.set_password(password)
        account.save()
        user_model.save()

        return account,user_model

class TeacherRegistrationSerializers(serializers.ModelSerializer):
    image = serializers.ImageField()
    confirm_password=serializers.CharField(required = True)
    educational_qualification=serializers.CharField()
    department=serializers.CharField()
    designation=serializers.CharField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password','image','educational_qualification','department','designation']
   
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        account_type = 'TEACHER'
        image = self.validated_data['image']
        educational_qualification = self.validated_data['educational_qualification']
        department = self.validated_data['department']
        designation = self.validated_data['designation']


        print(username,first_name,last_name,email,password,confirm_password,account_type,image)

        if password!=confirm_password:
            raise serializers.ValidationError({'error':"password didn't match"})
        # if password != '/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/':
        #     raise serializers.ValidationError({'error':'Please enter a strong password'})
        
        if User.objects.filter(email=email):
            raise serializers.ValidationError({'error':"Email already exist"})

        account = User(username=username,first_name=first_name,last_name=last_name,email=email)
        user_model = TeacherRegistrationModel(user=account,account_type=account_type,image=image,educational_qualification=educational_qualification,designation=designation,department=department)
        account.is_staff=True
        account.set_password(password)
        account.save()
        user_model.save()

        return account,user_model
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    class Meta:
        model = User



