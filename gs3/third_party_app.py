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

get_data(1)