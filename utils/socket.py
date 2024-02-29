import requests


def is_connected():
    try:
        # Attempt to send a request to google.com
        response = requests.get("http://www.google.com", timeout=5)
        # Check if the response status code is ok
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False


if is_connected():
    print("yes")
else:
    print("no")
