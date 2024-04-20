from django.shortcuts import redirect

def staff_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            result = func(request, *args, **kwargs)
        else:
            return redirect('dashboard:login')
        return result
    return wrapper