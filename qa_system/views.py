from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    """Simplified login view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # For demonstration, create a test admin user if it doesn't exist
        if not User.objects.filter(email='admin@example.com').exists():
            try:
                User.objects.create_superuser(
                    email='admin@example.com',
                    password='admin123',
                    first_name='Admin',
                    last_name='User',
                    role='admin',
                    sex='M'
                )
                print("Created test admin user: admin@example.com / admin123")
            except Exception as e:
                print(f"Could not create test user: {e}")
        
        # Try to authenticate
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Неверный email или пароль.')
    
    return render(request, 'auth/login.html')

# Mock the login_required decorator for testing purposes
def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        # For demo purposes, we'll just render the requested page
        # Comment this out if you want to enforce actual login
        return view_func(request, *args, **kwargs)
        
        # Uncomment this to enforce actual login
        # if request.user.is_authenticated:
        #     return view_func(request, *args, **kwargs)
        # else:
        #     messages.error(request, 'Пожалуйста, войдите в систему для доступа к этой странице.')
        #     return redirect('login')
    
    return wrapper

# Use our custom decorator instead of the built-in one (for testing)
# Uncomment the line below to enforce real login
# login_required = custom_login_required

def logout_view(request):
    """Placeholder logout view"""
    return redirect('login')

def main_view(request):
    """Main page view"""
    return render(request, 'main.html')

def registry_view(request):
    """Registry view"""
    return render(request, 'registry.html', {'chapters': []})

def create_view(request):
    """Create material view"""
    return render(request, 'create.html')

def create_material(request, material_type):
    """Handle creation of different material types"""
    messages.info(request, f'Creating {material_type} not yet implemented')
    return redirect('create')

def view_material(request, material_type, id):
    """View a specific material"""
    messages.info(request, f'Viewing {material_type} {id} not yet implemented')
    return redirect('registry')

def edit_material(request, material_type, id):
    """Edit a specific material"""
    messages.info(request, f'Editing {material_type} {id} not yet implemented')
    return redirect('registry')

def delete_material(request, material_type, id):
    """Delete a specific material"""
    messages.info(request, f'Deleting {material_type} {id} not yet implemented')
    return redirect('registry')

def control_view(request):
    """Control panel view"""
    messages.info(request, 'Control panel not yet implemented')
    return redirect('main')

def materials_view(request):
    """User's materials view"""
    messages.info(request, 'Materials view not yet implemented')
    return redirect('main')

def history_view(request):
    """History view - this is part of your assignment"""
    return render(request, 'history.html')

def view_revision(request, id):
    """View a specific revision"""
    messages.info(request, f'Viewing revision {id} not yet implemented')
    return redirect('history')

def compare_revisions(request, id1, id2):
    """Compare two revisions"""
    messages.info(request, f'Comparing revisions {id1} and {id2} not yet implemented')
    return redirect('history')

def system_view(request):
    """System settings view"""
    messages.info(request, 'System settings not yet implemented')
    return redirect('main')

def restore_material(request, material_type, id):
    """Restore a deleted material"""
    messages.info(request, f'Restoring {material_type} {id} not yet implemented')
    return redirect('system')

def update_pending_levels(request):
    """Update pending status levels"""
    messages.info(request, 'Updating pending levels not yet implemented')
    return redirect('system')

def people_view(request):
    """People management view"""
    messages.info(request, 'People management not yet implemented')
    return redirect('main')

def add_user(request):
    """Add a new user"""
    messages.info(request, 'Adding user not yet implemented')
    return redirect('people')

def edit_user(request, id):
    """Edit a user"""
    messages.info(request, f'Editing user {id} not yet implemented')
    return redirect('people')

def change_role(request, id):
    """Change user role"""
    messages.info(request, f'Changing role for user {id} not yet implemented')
    return redirect('people')

def block_user(request, id):
    """Block a user"""
    messages.info(request, f'Blocking user {id} not yet implemented')
    return redirect('people')

def unblock_user(request, id):
    """Unblock a user"""
    messages.info(request, f'Unblocking user {id} not yet implemented')
    return redirect('people')

def reset_password(request, id):
    """Reset user password"""
    messages.info(request, f'Resetting password for user {id} not yet implemented')
    return redirect('people')

def user_profile_view(request, id):
    """View user profile"""
    messages.info(request, f'Viewing profile for user {id} not yet implemented')
    return redirect('people')

def profile_view(request):
    """View own profile"""
    messages.info(request, 'Profile view not yet implemented')
    return redirect('main')

def guide_view(request):
    """Guide view"""
    messages.info(request, 'Guide not yet implemented')
    return redirect('main')

def notifications_view(request):
    """Notifications view"""
    messages.info(request, 'Notifications not yet implemented')
    return redirect('main')