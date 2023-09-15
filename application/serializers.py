from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . models import advocate, company


class companySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = company
        fields = '__all__'
    def get_employee_count(self, obj):
        count = obj.advocate_set.count()
        return count
        
        
class advocateSerializer(ModelSerializer):
    company = companySerializer()
    class Meta:
        model = advocate
        fields = ['username','bio','company']
