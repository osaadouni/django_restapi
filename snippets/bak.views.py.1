from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# View that supports listing all existing snippets, or create a new snippet
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

          
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update and delete a code snippet.
    """
    print(f"pk: {pk}")
    try: 
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        print("raise error")
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid(): 
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serialize.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(stats=204)
 
