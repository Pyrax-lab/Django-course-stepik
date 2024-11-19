
from rest_framework import serializers 
from blog.models import Post



# 1. Самый базовый сериализатор которые преобразует данные в формат json и обратно где поля должны совпадать с полями класса на основе которыго пишется сериализатор
class PostSerializer(serializers.Serializer):

    title = serializers.CharField(max_length = 250)
    body = serializers.CharField()
    publish = serializers.DateTimeField()


# 2. Класс где уже присутсвует методы create для создание обьекта на основе переданных данных и метод update для переопределения данных

class PostSerializer(serializers.Serializer):

    title = serializers.CharField(max_length = 250)
    body = serializers.CharField()
    publish = serializers.DateTimeField()


    def create(self, validated_data):
        return Post.objects.create(**validated_data)   
    
    def update(self, instance, validate_data):
        instance.title = validate_data.get("title", instance.title)
        instance.body  = validate_data.get("body", instance.body)
        instance.publish = validate_data.get("publish", instance.publish)


# 3. 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ("title", "body", "publish") # "__all__" для того чтобы в поле fields были все данные а не только те которые мы указали