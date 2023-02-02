from rest_framework import serializers
from .models import Post,Comments

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'comments')

    def get_comments(self, obj):
        comments = Comments.objects.filter(post=obj)
        return CommentSerializer(comments, many=True, context=self.context).data
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'comments',"author")
        
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    class Meta:
        model = Comments
        fields = ['id','comment','post','author']
    
