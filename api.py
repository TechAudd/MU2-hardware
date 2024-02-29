import requests

# Define the API endpoint URL
# Example API URL


def api_call(id):

    api_url = "https://api-dot-mahindrauni2.el.r.appspot.com/outpass/gateinout/1/" + id

# Make the API call
    response = requests.get(api_url)

# Check if the API call was successful
    if response.status_code == 200:
        # Access the JSON response
        json_response = response.json()

        # Store the entire JSON response in a variable
        data_from_api = json_response  # You can modify this based on your specific needs

        # Print the entire JSON response (for demonstration purposes)
        print("JSON response from the API:")
        print(data_from_api)
        return data_from_api
    else:
        print("Error: Failed to fetch data from the API")
        return "Error"
