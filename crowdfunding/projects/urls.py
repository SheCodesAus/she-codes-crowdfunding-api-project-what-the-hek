from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"),
    path('projects/filter', views.ProjectListFilter.as_view(), name="project-list-filter"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project-detail"),
    path('pledges/', views.PledgeList.as_view(), name="pledge-list"),
]

# can force it to use json or other language, may take out next session
urlpatterns = format_suffix_patterns(urlpatterns)