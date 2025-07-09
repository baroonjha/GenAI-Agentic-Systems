from urllib import response
import requests

# Make a GET request to the GitHub API
r=requests.get("https://api.github.com")

# Display all attributes and methods of the response object
# print(dir(r))

# Display the help documentation for the response object
# print(help(r))  

# Display the text content of the response
# print("Response Text:", r.text) 

# Display the status code of the response
# print("Status Code:", r.status_code)  

url="https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)

# print("Response Text:", response.text)

# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
#     # print("JSON Data:", data)
#     for post in data[:3]:
#         print(f"Title: {post['title']}") # Display the title of each post
#         print(f"Body: {post['body']}\n") # Display the body of each post
# else:
#     print("Failed to retrieve data:", response.status_code)


singlepost_url = "https://jsonplaceholder.typicode.com/posts/1"
singlepost_response = requests.get(singlepost_url)

data = singlepost_response.json()

# print("Single Post Response Text:", singlepost_response.text)
# print("Single Post JSON Data:", f"title: {data['title']}, body: {data['body']}")

payload={"page":2,"count":5}

r=requests.get("https://httpbin.org/get",params=payload)

print("GET Request with Parameters Response Text:", r.url)
payload={"name":"Alice","age":30}

r_post=requests.post("https://httpbin.org/post",data=payload)
# print("POST Request with Data Response Text:", r_post.text)

# Display the JSON response from the POST request
r_dict=r_post.json()
# print("POST Request JSON Data:", r_dict['form'])

    ## Optional Exploration      
user_url = "https://jsonplaceholder.typicode.com/users"
user_response=requests.get(user_url)
# print("User Response Text:", user_response.text)

if user_response.status_code == 200:
    user_data = user_response.json()
    print("First 2 Users:")
    for user in user_data[:2]:
        print(f"Name: {user['name']},Email:{user['email']}")
else:
    print("Failed to retrieve user data:", user_response.status_code)