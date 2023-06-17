from django.urls import path
from .views import InventoryMan, SignUp, Dashboard, FakaIzinto, Edit, Khipha
from django.contrib.auth import views as auth_views

urlpatterns = [
	path("", InventoryMan.as_view(), name="inventory-man"),
	path("signup/", SignUp.as_view(), name="signup"),
	path("dashboard/", Dashboard.as_view(), name="dashboard"),
 	path("add/", FakaIzinto.as_view(), name="faka"),
  	path("edit-item/<int:pk>", Edit.as_view(), name="change"),
   	path("delete-item/<int:pk>", Khipha.as_view(), name="khipha"),
	path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
	path("logout", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout")
]