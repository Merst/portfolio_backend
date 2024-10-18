from backend.models import Project, Skill, Category
from django.contrib.auth.models import User
from backend.serializers import ProjectSerializer, SkillSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'projects': reverse('project-list', request=request, format=format),
        'skills': reverse('skill-list', request=request, format=format)
    })

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions. Filtering on the attribute `older_project`
    (boolean) is also permitted.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['older_project', 'skills']