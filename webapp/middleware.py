from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Resolve the view function
        try:
            view_func = resolve(request.path_info).func
        except Resolver404:
            # If the URL doesn't resolve, let Django handle it (e.g., show a 404 page)
            return self.get_response(request)

        # Check for authentication
        if not request.user.is_authenticated:
            # Allow access to public URLs defined in settings
            if request.path_info in getattr(settings, 'PUBLIC_URLS', []):
                return self.get_response(request)

            # Allow access to views decorated with @public_route
            if getattr(view_func, 'is_public', False):
                return self.get_response(request)

            # Allow access to static and media files
            if settings.STATIC_URL and request.path_info.startswith(settings.STATIC_URL):
                return self.get_response(request)

            if getattr(settings, 'MEDIA_URL', None) and request.path_info.startswith(settings.MEDIA_URL):
                return self.get_response(request)

            # Redirect to login page if none of the above
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)
