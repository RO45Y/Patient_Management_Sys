from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Patient, Doctor, PatientDoctorMapping

User = get_user_model()

# -------------------- Register Serializer --------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        validators=[validate_password],
        error_messages={
            "blank": "Password cannot be blank.",
            "required": "Password is required."
        }
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'username': {'error_messages': {'blank': 'Username is required.'}},
            'email': {'error_messages': {'blank': 'Email is required.', 'invalid': 'Invalid email address.'}},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# -------------------- Patient Serializer --------------------
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['user']
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Patient name is required.'}},
            'age': {'error_messages': {'invalid': 'Age must be a number.'}},
            'gender': {'error_messages': {'blank': 'Gender is required.'}},
        }

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value

# -------------------- Doctor Serializer --------------------
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        extra_kwargs = {
            'name': {'error_messages': {'blank': 'Doctor name is required.'}},
            'specialization': {'error_messages': {'blank': 'Specialization is required.'}},
        }

# -------------------- Patient-Doctor Mapping Serializer --------------------
class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'

    def validate(self, data):
        # Prevent duplicate mapping
        if PatientDoctorMapping.objects.filter(patient=data['patient'], doctor=data['doctor']).exists():
            raise serializers.ValidationError("This mapping already exists.")
        return data
