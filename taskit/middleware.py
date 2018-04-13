"""Middleware for taskit."""
import re

from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


# pylint: disable=too-few-public-methods
class LoginRequiredMiddleware(object):
    """Login required for all urls except exemptions.

    Attributes:
        get_response (TYPE): Description
    """

    def __init__(self, get_response):
        """constructor."""
        self.get_response = get_response

    def __call__(self, request):
        """Caller."""
        return self.get_response(request)

    # pylint: disable=no-self-use,unused-argument
    def process_view(self, request, view_func, view_args, view_kwargs):
        """Main function to process the view.

        Args:
            request (TYPE): Description
            view_func (TYPE): Description
            view_args (TYPE): Description
            view_kwargs (TYPE): Description

        Returns:
            TYPE: redirect
        """
        original_path = request.path_info
        path = original_path.lstrip('/')
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        if not hasattr(request, 'user') or not request.user.is_authenticated():
            if not url_is_exempt:
                return redirect(settings.LOGIN_URL + '?next=' + original_path)
        elif url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return None
