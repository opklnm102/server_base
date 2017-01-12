from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # 로그인한 사용자(User)를 미리 기본 값으로 지정함
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'content', 'categories', 'created', 'modified')
        read_only_fields = ('id', 'user', 'created', 'modified')

    def update(self, instance, validated_data):
        # 수정시에 작성자(User)가 바뀌지 않게 지워줌
        del validated_data['user']
        return super(PostSerializer, self).update(instance, validated_data)
