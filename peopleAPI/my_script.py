import requests

BASE_URL = 'http://localhost:8000/'  # Replace with your API URL

def make_get_request():
    # Your GET request logic here
    pass

def make_post_request(data):
    url = BASE_URL + 'api/'
    headers = {'Content-Type':'multipart/form-data'}  # Set the content type
    response = requests.post(url, data=data, headers=headers)
    return response

def make_put_request(person_id, data):
    url = BASE_URL + f'api/{person_id}/'
    headers = {'Content-Type': 'multipart/form-data'}  # Set the content type
    response = requests.put(url, data=data, headers=headers)
    return response

def make_delete_request(person_id):
    url = BASE_URL + f'api/{person_id}/'
    response = requests.delete(url)
    return response

def make_custom_get_request():
    criteria = input("Enter the person's ID or full name: ")
    if criteria.isdigit():
        url = BASE_URL + f'api/{criteria}/'
    else:
        url = BASE_URL + f'api/?fullname={criteria}'
    response = requests.get(url)
    return response

# ... other request functions ...

if __name__ == "__main__":
    # You can add some test code here to run when this script is executed directly
    response = make_custom_get_request()
    print(response.status_code)
    print(response.text)
