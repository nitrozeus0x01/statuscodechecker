import requests

print("""

# WEB SITE STATUS CODE CHECKER #

>automated tools from Emre ASLAN<

	""")

site = input("Enter a site for checking : ")
print("")
site1 = requests.get(site)
print("Status Code Checked : ",site1.status_code)
print("Elapsed Time : ",site1.elapsed.total_seconds())
print("")
