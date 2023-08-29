from django.shortcuts import redirect


class AccessibleSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        if request.path != '/accessible_soon/':
            return redirect('appBlog:accessible_soon')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.


        return response