def public_route(view_func):
    """
    Decorator to mark a view as public, exempting it from the global authentication check.
    """
    def wrapper(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    wrapper.is_public = True
    return wrapper
