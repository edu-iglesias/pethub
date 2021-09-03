import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet

from pet_finder.serializers import PetFinderSerializer, ErrorDetailSerializer
from utils.address import get_full_address
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
        params = {
            'key': 'AIzaSyAdVP57aco-KOtMSFJHW4cBPgBvK3KG89I',
            'address': " 3355 Berkmar, Dr. Charlottesville, VA, US "
        }
        base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        response = requests.get(base_url, params=params).json()
        response.keys()
        user_latitude = ''
        user_longitude = ''
        if response['status'] == 'OK':
            geometry = response['results'][0]['geometry']
            user_latitude = geometry['location']['lat']
            user_longitude = geometry['location']['lng']

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

        animals_list = animals.get('animals')

        output_response = []
        for animal in animals_list:

            animal_dict = animal
            contact_dict = animal.get('contact')
            address_dict = contact_dict.get('address')

            address1 = address_dict.get('address1')
            address2 = address_dict.get('address2')
            city = address_dict.get('city')
            state = address_dict.get('state')
            country =  address_dict.get('country')

            full_address = get_full_address(address1, address2, city, state, country) # USE THIS ADDRESS TO GET LAT, LONG
            animal_dict["latitude"] = user_latitude  # INSERT LATITUDE HERE
            animal_dict["longitude"] = user_longitude  # INSERT LONGITUDE HERE

            output_response.append(animal_dict)

        return Response(output_response, status=HTTP_200_OK)


