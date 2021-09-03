from rest_framework import serializers


class PetFinderSerializer(serializers.Serializer):
    animal_id = serializers.IntegerField(required=False)
    animal_type = serializers.CharField(required=False)
    breed = serializers.CharField(required=False)
    size = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    age = serializers.CharField(required=False)
    color = serializers.CharField(required=False)
    coat = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    organization_id = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    distance = serializers.IntegerField(required=False)
    good_with_children = serializers.BooleanField(required=False)
    good_with_dogs = serializers.BooleanField(required=False)
    good_with_cats = serializers.BooleanField(required=False)
    house_trained = serializers.BooleanField(required=False)
    declawed = serializers.CharField(required=False)
    before_date = serializers.DateField(required=False)
    after_date = serializers.DateField(required=False)
    sort = serializers.DictField(required=False)
    pages = serializers.IntegerField(required=False, default=1)
    results_per_page = serializers.IntegerField(required=False, default=10)
    special_needs = serializers.CharField(required=False)
    return_df = serializers.BooleanField(default=False)

    class Meta:
        fields = [
            'animal_id',
            'animal_type',
            'breed',
            'size',
            'gender',
            'age',
            'color',
            'coat',
            'status',
            'name',
            'organization_id',
            'location',
            'distance',
            'good_with_children',
            'good_with_dogs',
            'good_with_cats',
            'house_trained',
            'declawed',
            'before_date',
            'after_date',
            'sort',
            'pages',
            'results_per_page',
            'return_df'
            'special_needs'
        ]

class ErrorDetailSerializer(serializers.Serializer):
    error = serializers.CharField(max_length=255)