import requests

def mailServer (urls):        
    results = []
    
    for url in urls:
        response = requests.get(url)
        
        if response.status_code in [200, 302]:
            results.append("OK")
        else:
            results.append("FAIL")
    return results

urls = [ "https://2ch.hk" ]

results = mailServer(urls)

print(results)       # Enter result  