
from django.http import JsonResponse

def post_details (request , id):
    return JsonResponse({"id" : id})