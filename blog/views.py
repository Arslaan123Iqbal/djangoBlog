
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Post
from .serializers import PostSerializer,CommentSerializer
# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        print(request.user)
        instance = serializer.save()
        instance.author = request.user
        instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_comment(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except:
        return Response({"error":"Post does not exist"})
    data = request.data
    data['post'] = post.id
    serialize = CommentSerializer(data=data)
    if serialize.is_valid():
        instance = serialize.save()
        instance.author = request.user
        instance.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    post_serialized = PostSerializer(posts, many=True, context={'request': request})
    return Response(post_serialized.data)