from django.urls import path, include

urlpatterns = [
    path('', include("apps.core.urls")),
    path('groups/', include("apps.groups.urls")),
    path('teachers/', include("apps.teachers.urls")),
    path('students/', include("apps.students.urls")),
    path('lessons/', include("apps.lessons.urls")),
    path('telegram-users/', include("apps.telegram_users.urls")),
    path('products/', include("apps.products.urls")),
]
