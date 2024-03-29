"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from calculator.views import home_view, calculate_recipe_view
from django.urls import path

# urlpatterns = [
#     # здесь зарегистрируйте вашу view-функцию
#     path('admin/', admin.site.urls),
#     path('recipes/', home_view, name='home'),
#     path('recipies/<recipe_name>/', calculate_recipe_view, name='calculate_recipe'),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', home_view, name='home'),
    path('recipes/<recipe_name>/', calculate_recipe_view, name='calculate_recipe')
]