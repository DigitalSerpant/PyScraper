import os
import requests
from bs4 import BeautifulSoup

url = input("enter the url of the website: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Create a directory with the name of the website
website_name = url.split('//')[-1].split('/')[0]
os.makedirs(website_name, exist_ok=True)

# Extract all the HTML code from the page
html_code = str(soup)
with open(f'{website_name}/index.html', 'w') as f:
    f.write(html_code)
    print("Html is Complete")

# Extract all the JavaScript code from the page
script_tags = soup.find_all('script')
for i, tag in enumerate(script_tags):
    if tag.has_attr('src'):
        # The script is external, so fetch the content from the URL
        script_url = tag['src']
        script_response = requests.get(script_url)
        script_code = script_response.text
        with open(f'{website_name}/script_{i}.js', 'w') as f:
            f.write(script_code)
            print("Js is Complete but the script is external")
    else:
        # The script is inline, so just extract the code
        script_code = tag.string
        with open(f'{website_name}/script_{i}.js', 'w') as f:
            f.write(script_code)
            print("Js is Complete")

# Extract all the CSS code from the page
css_tags = soup.find_all('style')
for i, tag in enumerate(css_tags):
    css_code = tag.string
    with open(f'{website_name}/style_{i}.css', 'w') as f:
        f.write(css_code)
        print("css is Complete")

print("Complete!")
