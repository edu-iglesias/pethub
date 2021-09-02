from rest_framework import serializers


class PetFinderSerializer(serializers.Serializer):
    animal_id = serializers.IntegerField()
    animal_type = serializers.CharField()
    breed = serializers.CharField()
    size = serializers.CharField()
    gender = serializers.CharField()
    age = serializers.CharField()
    color = serializers.CharField()
    coat = serializers.CharField()
    status = serializers.CharField()
    name = serializers.CharField()
    organization_id = serializers.CharField()
    location = serializers.CharField()
    distance = serializers.IntegerField()
    good_with_children = serializers.BooleanField()
    good_with_dogs = serializers.BooleanField()
    good_with_cats = serializers.BooleanField()
    house_trained = serializers.BooleanField()
    declawed = serializers.CharField()
    before_date = serializers.CharField()
    after_date = serializers.CharField()
    sort = serializers.DictField()
    pages = serializers.IntegerField()
    results_per_page = serializers.IntegerField()
    return_df = serializers.BooleanField(False)


    class Meta:
        fields = [
            'animal_id',
            'animal_type',
            'breed',
            'contact_number',
        ]