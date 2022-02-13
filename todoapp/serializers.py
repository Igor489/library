from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Project
from .models import ToDo
from userapp.serializers import UserSerializer
from userapp.models import User


class ProjectSerializer(ModelSerializer):
    # Настройка сериализатора
    # Настройка Foreign Key
    # owner = HyperlinkedIdentityField(view_name='user-detail')
    # Настройка Many to many
    # users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectReadSerializer(ModelSerializer):
    # Настройка сериализатора
    # Настройка Foreign Key
    # owner = HyperlinkedIdentityField(view_name='user-detail')
    # Настройка Many to many
    # users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        # exclude = ('is_active',)
        fields = '__all__'


class ToDoReadSerializer(ModelSerializer):
    # project = HyperlinkedIdentityField(view_name='project-detail')
    # creator = HyperlinkedIdentityField(view_name='user-detail')
    project = StringRelatedField()
    creator = StringRelatedField()

    class Meta:
        model = ToDo
        # exclude = ('is_active',)
        fields = '__all__'
