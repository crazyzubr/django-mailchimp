from django.contrib import admin
from mailchimp.models import Campaign
from mailchimp.settings import VIEWS_OVERVIEW
import mailchimp.views


class MailchimpAdmin(admin.ModelAdmin):
    def get_urls(self):
        from django.conf.urls import url
        urlpatterns = [
            url(r'^$',
                mailchimp.views.overview,
                name='mailchimp_campaign_changelist',
                kwargs={'page':'1'}),
        ]
        return urlpatterns
    
    def has_add_permission(self, request):
        # disable the 'add' button
        return False
    
    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('mailchimp.can_view')
        
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Campaign, MailchimpAdmin)
