import requests

from requests.exceptions import ConnectionError,RequestException,Timeout

import time


#Global variable
previous_state = None

def check_website(url):
    if not url.startswith(("http://","https://")):
        url = "https://" + url

    try :
        req_response = requests.head(url,timeout=5,allow_redirects=True)

        # To get the response time of a website
        time_elapsed = req_response.elapsed
        current_status_code = req_response.status_code

        if 200 <= current_status_code < 400 :
            website_status = "UP"
            global previous_state
            if website_status != previous_state:
                print(f"Alert! Status changed from {previous_state} to {website_status}")
                previous_state = website_status

            return f" {url} - {website_status} - {current_status_code} - {time_elapsed.total_seconds() * 1000:.2f} ms "
        else:
            website_status = "DOWN"
            if website_status != previous_state:
                print(f"Alert! Status changed from {previous_state} to {website_status}")
                previous_state = website_status

            return f" {url} - {website_status} - {current_status_code} - {time_elapsed.total_seconds() * 1000:.2f} ms "


    except ConnectionError:
        website_status = "DOWN"
        if website_status != previous_state:
            print(f"Alert! Status changed from {previous_state} to {website_status}")
            previous_state = website_status
        return "DOWN (Connection Error)"

    except Timeout:
        website_status = "DOWN"
        if website_status != previous_state:
            print(f"Alert! Status changed from {previous_state} to {website_status}")
            previous_state = website_status
        return "DOWN (Request Timed Out)"

    except RequestException as e :
        website_status = "DOWN"
        if website_status != previous_state:
            print(f"Alert! Status changed from {previous_state} to {website_status}")
            previous_state = website_status
        return f"DOWN (Error: {e})"


# Example Usage
while True:
    print("Local Server:", check_website("http://localhost:8000"))
    time.sleep(45)
#print("other-site:", check_website("https://kraftnest.netlify.app/"))
#print("invalid-site:", check_website("thisisnotarealsite12345.com"))

'''
TO DO : 
NEXT TASK : The program should handle multiple sites instead of just one site

What the project does,in one sentence: it watches a list of websites and alerts you when any one of them goes down or comes back.
'''