import requests

# Define the base URL of your Django API
base_url = 'http://127.0.1:8000/'  # Replace with your actual API URL

# Prompt the user to enter the criteria (id or name)
criteria = input("Enter the person's ID or full name: ")

# Determine whether the criteria is an id or a name
if criteria.isdigit():
    # If it's a digit, assume it's an id
    url = base_url + f'api/{criteria}/'
else:
    # If it's not a digit, assume it's a name
    url = base_url + f'api/?fullname={criteria}'

# Define headers for application/x-www-form-urlencoded
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Send a GET request to retrieve the person with headers
retrieve_response = requests.get(url, headers=headers)

# Print the response for the GET request
print('Retrieve Response:')
print('Status Code:', retrieve_response.status_code)
print('Response Content:', retrieve_response.text)

# Extract the person's ID from the response JSON
person_id = None
if retrieve_response.status_code == 200:
    person_data = retrieve_response.json()
    if person_data:
        person_id = person_data[0]['id']

# Prompt the user to enter the person's full name and track
fullname = input("Enter the person's full name: ")
track = input("Enter the person's track: ")

# Define the updated data for the PUT request
updated_person_data = {
    'fullname': fullname,
    'track': track,
}

# Send a PUT request to update the person's data (based on either id or name) with headers
if person_id is not None:
    update_url = base_url + f'api/{person_id}/'
    update_response = requests.put(update_url, data=updated_person_data, headers=headers)

    # Print the response for the PUT request
    print('\nUpdate Response:')
    print('Status Code:', update_response.status_code)
    print('Response Content:', update_response.text)

# Send a DELETE request to delete the person (based on either id or name) with headers
if person_id is not None:
    delete_url = base_url + f'api/{person_id}/'
    delete_response = requests.delete(delete_url, headers=headers)

    # Print the response for the DELETE request
    print('\nDelete Response:')
    print('Status Code:', delete_response.status_code)
