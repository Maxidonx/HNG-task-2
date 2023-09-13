# peopleAPI/sql_injection_mitigation.py
from .models import Person  # Import your actual model

def retrieve_data_safely(input_param):
    # Use Django ORM to safely retrieve data
    try:
        results = Person.objects.filter(fullname=input_param)  # Using the 'fullname' field
        return results
    except Person.DoesNotExist:
        return None
