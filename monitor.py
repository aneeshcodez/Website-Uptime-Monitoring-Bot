from checker import check_website

sites = [
    "https://jsonplaceholder.typicode.com/",
    "https://this-site-does-not-exist-98765.com",
    "http://localhost:8000"
]

def check_multiple_sites(sites):
    for site in sites :
        each_site_result = check_website(site)
        print(each_site_result)


check_multiple_sites(sites)
