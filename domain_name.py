from urllib.parse import urlsplit

def domain_name(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    # Use urlsplit to parse the URL
    parsed_url = urlsplit(url)
    
    # Get the netloc part (domain) and remove any leading "www."
    domain_name = parsed_url.netloc.replace("www.", "")
    
    main_domain = domain_name.split('.')[0]
    
    return main_domain

# Examples
url1 = "http://github.com/carbonfive/raygun"
result1 = domain_name(url1)
print(result1)  # Output: "github"

url2 = "http://www.zombie-bites.com"
result2 = domain_name(url2)
print(result2)  # Output: "zombie-bites"

url3 = "https://www.cnet.com"
result3 = domain_name(url3)
print(result3)  # Output: "cnet"

url4 = "www.xakep.ru"
result4 = domain_name(url4)
print((result4))