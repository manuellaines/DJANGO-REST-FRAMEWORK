from .models import *
from rest_framework.serializers import ModelSerializer

class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AlbumSerializer(ModelSerializer):
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'

class BookingSerializer(ModelSerializer):
    album = AlbumSerializer()
    contact = ContactSerializer()

    class Meta:
        model = Booking
        fields = '__all__'
