# to covert python to json
from rest_framework.serializers import ModelSerializer
from.models import userprofile

class userser(ModelSerializer):
    class Meta:
        model=userprofile
        fields='__all__'
        