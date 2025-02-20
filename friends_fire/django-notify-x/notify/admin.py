from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'actor', 'verb',
                    'obj', 'target', 'read', 'deleted')
    list_filter = ('read', 'deleted', 'nf_type', 'created')
    search_fields = ('recipient__username', 'verb', 'description')

    fieldsets = (
            ('Basic details',
                {'fields': ('recipient', 'verb', 'description', 'nf_type')}),

            ('Actor details',
                {'fields': ('actor_content_type', 'actor_object_id',
                            'actor_text', 'actor_url_text')}),

            ('Object details',
                {'fields': ('obj_content_type', 'obj_object_id',
                            'obj_text', 'obj_url_text')}),

            ('Target details',
                {'fields': ('target_content_type', 'target_object_id',
                            'target_text', 'target_url_text')}),

            ('Other details',
                {'fields': ('extra', 'read', 'deleted')}),
        )
