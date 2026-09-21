from django.http import JsonResponse


def post_list (request):
    return JsonResponse({"response" : "ok"})