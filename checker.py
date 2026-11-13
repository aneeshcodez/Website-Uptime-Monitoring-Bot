import requests

from requests.exceptions import ConnectionError,RequestException,Timeout

import time

def check_website(url):
    if not url.startswith(("http://","https://")):
        url = "https://" + url

    try :
        req_response = requests.head(url,timeout=5,allow_redirects=True)

        # To get the response time of a website
        time_elapsed = req_response.elapsed

        if 200 <= req_response.status_code < 400 :
            return f" {url} - UP - {req_response.status_code} - {time_elapsed.total_seconds() * 1000:.2f} ms "
            # return f"UP(Status Code: {req_response.status_code})"
        else:
            return f"DOWN"

    except ConnectionError:
        return "DOWN (Connection Error)"
    except Timeout:
        return "DOWN (Request Timed Out)"
    except RequestException as e :
        return f"DOWN (Error: {e})"


# Example Usage
while True:
    print("google.com:", check_website("google.com"))
    time.sleep(45)
#print("other-site:", check_website("https://kraftnest.netlify.app/"))
#print("invalid-site:", check_website("thisisnotarealsite12345.com"))