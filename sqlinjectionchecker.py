#SQL injection checker

import requests

def check_sql_injection(url):
    injection_strings = ["'", "\"", ";", "--", "/*", "*/"]
    for string in injection_strings:
        payload = f"{url}{string}"
        response = requests.get(payload)
        if "error" in response.text.lower() or "syntax" in response.text.lower():
            print(f"Possible SQL injection vulnerability found with payload: {payload}")
        else:
            print(f"Payload: {payload} did not trigger any SQL error.")
            
if __name__ == "__main__":
    url = "https://www.w3schools.com/php/php_mysql_search.asp?searchterm="
    check_sql_injection(url)
    
    