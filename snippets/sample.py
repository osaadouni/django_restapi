from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser

import io 

snippet = Snippet(code='foo = "bar"\nprint(f"foo: {foo}")\n')

# serialize the snippet instance  ( produce python native datatype ) 
serializer = SnippetSerializer(snippet)
print(serializer.data)

# render json from the Python native datatype 
content = JSONRenderer().render(serializer.data)
print(content)



# deserialize is similar.  First we parse a stream into Python native datatypes 
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# restore native datatype into a fully populated object instance
serializer = SnippetSerializer(data=data)
serializer.is_valid()

print(serializer.validated_data)

serializer.save()

serializer = SnippetSerializer(Snippet.objects.all(), many=True)
print(serializer.data)


