from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import (
    User, Chapter, Section, Subsection, QA, QA_Subsection, QA_Reference,
    RevisionHistory, Log
)

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'organization')
    ordering = ('last_name', 'first_name')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'patronymic', 'sex', 'birth_date')}),
        (_('Contact info'), {'fields': ('region', 'address', 'organization', 'position', 'phone')}),
        (_('Permissions'), {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('registration_date', 'last_login')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'role', 'is_active', 'is_staff'),
        }),
    )

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'author', 'status', 'is_published', 'is_deleted')
    list_filter = ('status', 'is_published', 'is_deleted')
    search_fields = ('title',)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'status', 'is_published', 'is_deleted')
    list_filter = ('status', 'is_published', 'is_deleted', 'chapter')
    search_fields = ('title',)

class SubsectionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'status', 'is_published', 'is_deleted')
    list_filter = ('status', 'is_published', 'is_deleted', 'section__chapter')
    search_fields = ('title',)

class QAAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'status', 'is_published', 'is_deleted')
    list_filter = ('status', 'is_published', 'is_deleted')
    search_fields = ('question', 'answer')

class QA_SubsectionAdmin(admin.ModelAdmin):
    list_display = ('qa', 'subsection', 'copy_number', 'number')
    list_filter = ('subsection__section__chapter',)
    search_fields = ('qa__question', 'subsection__title')

class QA_ReferenceAdmin(admin.ModelAdmin):
    list_display = ('qa', 'url', 'description')
    search_fields = ('qa__question', 'description', 'url')

class RevisionHistoryAdmin(admin.ModelAdmin):
    list_display = ('material_type', 'material_id', 'material_title', 'editor', 'status', 'written_at')
    list_filter = ('material_type', 'status')
    search_fields = ('material_title', 'editor__email')

class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_type', 'created_at')
    list_filter = ('action_type',)
    search_fields = ('user__email', 'action_type')
    readonly_fields = ('user', 'action_type', 'action_details', 'created_at')

# Register the models with their respective admin classes
admin.site.register(User, UserAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(QA, QAAdmin)
admin.site.register(QA_Subsection, QA_SubsectionAdmin)
admin.site.register(QA_Reference, QA_ReferenceAdmin)
admin.site.register(RevisionHistory, RevisionHistoryAdmin)
admin.site.register(Log, LogAdmin)