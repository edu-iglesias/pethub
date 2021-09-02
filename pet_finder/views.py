from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet

from pet_finder.serializers import PetFinderSerializer
from utils.petfinder import pet_finder_generate_token


class PetFinderView(ViewSet):

    @swagger_auto_schema(
        method='POST',
        request_body=PetFinderSerializer,
    )
    @action(methods=["POST"], detail=False, permission_classes=[], authentication_classes=[])
    def animals(self, request):
        """
        Parameters
        ----------
        animal_id : int, tuple or list of int, optional
        animal_type : {'dog', 'cat', 'rabbit', 'small-furry', 'horse', 'bird', 'scales-fins-other', 'barnyard'},
        breed: str, tuple or list of str, optional
        size: {'small', 'medium', 'large', 'xlarge'}, str, tuple or list of str, optional
        gender : {'male', 'female', 'unknown'} str, tuple or list of str, optional
        age : {'baby', 'young', 'adult', 'senior'} str, tuple or list of str, optional
        color : str, optional
        coat : {'short', 'medium', 'long', 'wire', 'hairless', 'curly'}, str, tuple or list of str, optional
        status : {'adoptable', 'adopted', 'found'} str, optional
        name : str, optional
        organization_id : str, tuple or list of str, optional
        location : str, optional
        distance : int, optional (defaults 100 miles, max 500 miles)
        good_with_children : bool, optional
        good_with_cats : bool, optional
        good_with_dogs : bool, optional
        declawed : bool, optional
        special_needs : bool, optional
        house_trained : bool, optional
        before_date : str, datetime
        after_date : str, datetime
        sort : {'recent', '-recent', 'distance', '-distance'}, optional
        pages : int, default 1
        results_per_page : int, default 20
        return_df : boolean, default False
        """

        data = request.data

        pf = pet_finder_generate_token()

        animals = pf.animals(
            animal_id=data.get('animal_id', None),
            animal_type=data.get('animal_type', None),
            breed=data.get('breed', None),
            size=data.get('size', None),
            gender=data.get('gender', None),
            age=data.get('age', None),
            color=data.get('color', None),
            coat=data.get('coat', None),
            status=data.get('status', None),
            name=data.get('name', None),
            organization_id=data.get('organization_id', None),
            location=data.get('location', None),
            distance=data.get('distance', None),
            good_with_children=data.get('good_with_children', None),
            good_with_dogs=data.get('good_with_dogs', None),
            good_with_cats=data.get('good_with_cats', None),
            house_trained=data.get('house_trained', None),
            declawed=data.get('declawed', None),
            special_needs=data.get('special_needs', None),
            before_date=data.get('before_date', None),
            after_date=data.get('after_date', None),
            sort=data.get('sort', None),
            pages=data.get('pages', 1),
            results_per_page=data.get('results_per_page', 10),
            return_df=data.get('return_df', False)
        )

        return Response(animals, status=HTTP_200_OK)


