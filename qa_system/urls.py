from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Main pages
    path('', views.main_view, name='main'),
    path('registry/', views.registry_view, name='registry'),
    path('create/', views.create_view, name='create'),
    path('create/<str:material_type>/', views.create_material, name='create_material'),
    
    # Material views
    path('material/<str:material_type>/<int:id>/', views.view_material, name='view_material'),
    path('material/<str:material_type>/<int:id>/edit/', views.edit_material, name='edit_material'),
    path('material/<str:material_type>/<int:id>/delete/', views.delete_material, name='delete_material'),
    
    # Control panel
    path('control/', views.control_view, name='control'),
    
    # Materials management
    path('materials/', views.materials_view, name='materials'),
    
    # History
    path('history/', views.history_view, name='history'),
    path('revision/<int:id>/', views.view_revision, name='view_revision'),
    path('revision/compare/<int:id1>/<int:id2>/', views.compare_revisions, name='compare_revisions'),
    
    # System settings
    path('system/', views.system_view, name='system'),
    path('system/restore/<str:material_type>/<int:id>/', views.restore_material, name='restore_material'),
    path('system/update-pending-levels/', views.update_pending_levels, name='update_pending_levels'),
    
    # User management
    path('people/', views.people_view, name='people'),
    path('people/add/', views.add_user, name='add_user'),
    path('people/<int:id>/edit/', views.edit_user, name='edit_user'),
    path('people/<int:id>/change-role/', views.change_role, name='change_role'),
    path('people/<int:id>/block/', views.block_user, name='block_user'),
    path('people/<int:id>/unblock/', views.unblock_user, name='unblock_user'),
    path('people/<int:id>/reset-password/', views.reset_password, name='reset_password'),
    path('people/<int:id>/profile/', views.user_profile_view, name='user_profile'),
    
    # Profile
    path('profile/', views.profile_view, name='profile'),
    
    # Guide
    path('guide/', views.guide_view, name='guide'),
    
    # Notifications
    path('notifications/', views.notifications_view, name='notifications'),
]
