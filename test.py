from bs4 import BeautifulSoup
from django.urls import reverse

# Assuming you have the HTML content in a variable named 'html_content'
# You can replace this with your actual HTML content

html_content = """
<body></body>
"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")


# Iterate through all 'a' tags and update the 'href' attribute
for a_tag in soup.find_all("a", href=True):
    a_tag["href"] = f'{{% url "home" %}}'

# Print the modified HTML content
print(soup.prettify())
