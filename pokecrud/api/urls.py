from django.urls import path
from .views import ApiListView, ApiCreateView, ApiDetailView, ApiUpdateView, ApiDeleteView

app_name="blog"

urlpatterns = [
    path('', ApiListView.as_view(), name="home"),
    path('create/', ApiCreateView.as_view(), name="create"),
    path('<int:pk>/', ApiDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', ApiUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', ApiDeleteView.as_view(), name="delete")

]