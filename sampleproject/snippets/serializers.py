from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    """
    read_only = True --> only get
    """
    title = serializers.CharField(required = False, allow_blank = True, max_length = 100)
    code = serializers.CharField(style = {'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required = False)
    language = serializers.ChoiceField(choices = LANGUAGE_CHOICES, default = 'python')
    style = serializers.ChoiceField(choices = STYLE_CHOICES, default = 'friendly')


    """
    funtion names "create" and "update" are predefined names so no need to actually call it
    like SnippetSerializer.create()
    """
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)
    """
    how to use this create funtion 

    a = SnippetSerializer(data = {"code": "PostgreSQL Query"})  NOTE: only 1 argument is passed
    if a.is_valid():
        a.save()
    """
    
    def update(self, instance: Snippet, validated_data):
        """
        Update and return an existing `Snippet app` instance, given the validated data.
        it only update because instance.id is not included below
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()

        return instance
    """
    how to call this

    b = Snippet.objects.get(pk = 1)
    bb = SnippetSerializer(b, data = {"code": "PostgreSQL Query"})  NOTE: 2 arguments passed
    if bb.is_valid():
        bb.save()
    """
    
