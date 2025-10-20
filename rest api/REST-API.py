# http methods
#    1:get (to retrieve data think as you are reading)
#    2:post (to add new resource or data on server)
#    3:push (to update previous data or resource entirely)
#    4:patch (to update only one field of previous resource)
#    6:delete (to delete a specific resource)



#  Common HTTP Status Codes (with Meaning)
# Code	  Name	                Meaning                                             Use Case
# 200	     OK	                  Request was successful.                   Used with GET, PUT, DELETE.
# 201	     Created	          A new resource was created.                    Used with POST.
# 204	     No Content	          Request was successful but there is         (e.g., after a DELETE).
#                               no content to return                     
# 400	     Bad Request	      The request was invalid (                e.g., missing data or wrong format).
# 401	     Unauthorized	      Authentication is required or failed.
# 403	     Forbidden	          You are not allowed to access this resource.
# 404	     Not Found	          The resource was not found.
# 500	     Internal             Something went wrong on the server side.
#          Server Error	                    




# api endpoint : it is a url your application use to access web service .A single api can have multiple endpoints like (books , customers etc)
# base url :  endpoint url consist of base url and placeholder (www.abc.com   it is a base url)
# placeholder :  placeholder is like an id which you use to access a resource (www.abc.com/books/123  books/123 is a placeholder)


                                          # get request

import requests

url1 = 'https://jsonplaceholder.typicode.com/todos/2'

try:
    response =requests.get(url1)
    # Check if the request was successful (status code 200)
    response.raise_for_status()

    # The response data is a JSON string.
    # The .json() method converts it into a Python dictionary.
    data = response.json()
    print("API data \n")
    print(data)

    # access specific parts of the dictionary
    print("\n title is " , data.get("title"))
    print("status is :", response.status_code)


except requests.exceptions.RequestException as e:
    print(f"error occures as {e}")






                                            #  post request

import json
api_url = "https://jsonplaceholder.typicode.com/todos"
new_todo = {
    "userId": 1,
    "title": "Learn to use POST requests",
    "completed": False
}
try:
    response1 = requests.post(api_url ,json=new_todo)
    response1.raise_for_status()

    data = response1.json()

    print("Request successful. New resource created.")
    print("Status Code:", response.status_code)
    print("New Todo Data:")
    print(json.dumps(data, indent=4))

except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the request
    print(f"An error occurred: {e}")








                                            # put request
import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos/1"

new_todo_data = {
    "userId": 1,
    "id": 1,
    "title": "This is the updated title for the to-do item.",
    "completed": True
}

try:
 
    response = requests.put(api_url, json=new_todo_data)

    response.raise_for_status()

    updated_data = response.json()

    print("Request successful! Resource updated.")
    print("Status Code:", response.status_code)
    print("Updated Todo Data:")
    print(json.dumps(updated_data, indent=4))

except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the request
    print(f"An error occurred: {e}")








                                              # patch request

import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos/1"

patch_data = {
    "title": "This is a new title from a PATCH request."
}

try:
    response = requests.patch(api_url, json=patch_data)

    response.raise_for_status()

    updated_data = response.json()

    print("Request successful! Resource partially updated.")
    print("Status Code:", response.status_code)
    print("Updated Todo Data (notice only the title has changed):")
    print(json.dumps(updated_data, indent=4))

except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the request
    print(f"An error occurred: {e}")








                                                # delete request

import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response4 = requests.delete(api_url)
    response4.raise_for_status()

    print(f"Request successful! Resource at {api_url} was deleted.")
    print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
     print(f"An error occurred: {e}")

