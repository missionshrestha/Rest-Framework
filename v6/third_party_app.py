import requests
import json

URL="http://127.0.0.1:8000/studentapi/"




def get_data(id=None):
    """
    Fetches data from a specified URL using the GET method.

    Args:
        id (int, optional): The ID of the data to fetch. Defaults to None.

    Returns:
        dict: The fetched data in JSON format.

    Example:
        >>> get_data(1)
        {'id': 1}

    This function takes an optional ID parameter and constructs a JSON payload based on the ID value. It then sends a GET request to the specified URL with the constructed payload. The response is then parsed as JSON and returned as a dictionary.

    The function can be used as follows:
    - To fetch all data: get_data()
    - To fetch data with a specific ID: get_data(id=1)
    """


    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

# Call the get_data() function to fetch all data
# get_data()

def post_data():
    """
    Sends a POST request to the specified URL with a JSON payload.

    Returns:
        dict: The response data in JSON format.

    Example:
        >>> post_data()
        {'id': 2, 'name': 'Devi', 'roll': 105, 'city': 'Mumbai'}

    This function constructs a JSON payload with the name, roll, and city values. It then sends a POST request to the specified URL with the constructed payload. The response is then parsed as JSON and returned as a dictionary.

    The function can be used as follows:
    post_data()
    """
    data = {
        'name': 'Tej',
        'roll': 106,
        'city': 'Mumbai'
    }
    
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

# Call the post_data() function to send a POST request
# post_data()


def update_data():
    """
    Updates data on the specified URL using the PUT method.

    Example:
        >>> update_data()

    This function demonstrates how to update data on the specified URL using the PUT method. It can be used to perform both partial and complete updates.

    To perform a partial update, provide the ID and the fields to update in the `data` dictionary. For example:
    ```
    data = {
        'id': 5,
        'name': 'Niru',
    }
    ```
    This will update the 'name' field of the data with ID 5.

    To perform a complete update, provide all the fields in the `data` dictionary. For example:
    ```
    data = {
        'id': 6,
        'name': 'Siru',
        'roll': 106,
        'city': 'USA'
    }
    ```
    This will update all the fields of the data with ID 6.

    After constructing the JSON payload from the `data` dictionary, a PUT request is sent to the specified URL with the payload. The response is then parsed as JSON and printed.

    Note: Uncomment the desired `data` dictionary to perform either a partial or complete update.
    """

    # Partial update
    data = {
        'id': 10,
        'name': 'Niru',
    }
    
    # # Complete update
    # data = {
    #     'id': 6,
    #     'name': 'Siru',
    #     'roll': 106,
    #     'city': 'USA'
    # }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()




def delete_data():
    """
    Deletes data from the specified URL using the DELETE method.

    Example:
        >>> delete_data()

    This function demonstrates how to delete data from the specified URL using the DELETE method. It takes an ID parameter and constructs a JSON payload with the ID value. It then sends a DELETE request to the specified URL with the constructed payload. The response is then parsed as JSON and printed.

    The function can be used as follows:
    delete_data()
    """

    # Specify the ID of the data to delete
    data = {
        'id': 13,
    }

    # Convert the data dictionary to JSON format
    json_data = json.dumps(data)

    # Send a DELETE request to the specified URL with the JSON payload
    r = requests.delete(url=URL, data=json_data)

    # Parse the response as JSON
    data = r.json()

    # Print the response data
    print(data)

# Call the delete_data() function to delete data
# delete_data()



# function caller

# get_data()
# post_data()
# update_data()
delete_data()