from .models import ActivityLog
from django.utils.deprecation import MiddlewareMixin

class LogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        url = request.build_absolute_uri()
        ActivityLog.objects.create(ip_address=ip_address, url=url)
