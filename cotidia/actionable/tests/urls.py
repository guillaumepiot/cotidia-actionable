from django.urls import path, include

urlpatterns = [
    path('actionable', include("cotidia.actionable.urls.admin", namespace="actionable-admin")),
    path('account', include("cotidia.account.urls.admin",
                            namespace="account-admin")),
    path('mail', include("cotidia.mail.urls",
                         namespace="mail-admin")),
    path('admin', include("cotidia.admin.urls.admin",
                          namespace="generic-admin")),
    path('dashboard', lambda x: None, name="dashboard")
    ]
