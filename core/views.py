from django.shortcuts import render

# Create your views here.


def index(request):
    return render(
        request,
        'index.html'
    )


# 400 Bad Request
def error_400(request, exception):
    return render(request, "400.html", status=400)


# 403 Forbidden
def error_403(request, exception):
    return render(request, "403.html", status=403)


# 404 Not Found
def error_404(request, exception):
    return render(request, "404.html", status=404)


# 429 Too Many Requests
def error_429(request, exception):
    return render(request, "429.html", status=429)


# 500 Internal Server Error
def error_500(request, exception):
    return render(request, "500.html", status=500)


# 503 Service Unavailable
def error_503(request, exception):
    return render(request, "503.html", status=503)
