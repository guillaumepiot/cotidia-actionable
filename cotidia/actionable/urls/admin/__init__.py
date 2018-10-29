from django.urls import path, include

app_name = "actionable"
urlpatterns = [
    path('actionable/',
        include("cotidia.actionable.urls.admin.actionable")),
    ]
