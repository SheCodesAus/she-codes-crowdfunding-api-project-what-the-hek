from rest_framework import serializers

from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter',]
        read_only_fields = ['id', 'supporter']
        # or this does the same
        # fields = '__all__'

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner_id')

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class ProjectDetailSerializer(ProjectSerializer):
    # class Meta:
    #     model = Pledge
    #     read_only_fields = ['amount']

    pledges = PledgeSerializer(many=True, read_only=True)

    
    # queryset = Pledge.objects.filter(anonymous=False)

    # for anon in pledges:
    #     if 'anonymous' == False
    #             pledges = PledgeSerializer(many=True, read_only=True)
        # print('There are no pledges')

# class ProjectDetailSerializer(serializers.ModelSerializer):
#     pledges = serializers.SerializerMethodField()

#     def view_pledges(self, ):
#         queryset = Pledge.objects.filter(anonymous=False)
#         pledges = PledgeSerializer(many=True, read_only=True)
#         serializer = LikeSerializer(instance=queryset, many=True)
#         return serialzer.data
#     class Meta:
#         model = Pledge