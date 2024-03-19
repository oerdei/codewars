def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
    
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