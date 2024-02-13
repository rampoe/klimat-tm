from bs4 import BeautifulSoup

html_content = """
"""

soup = BeautifulSoup(html_content, "html.parser")

for a_tag in soup.find_all("a", href=True):
    a_tag["href"] = f'{{% url "home" %}}'

print(soup.prettify())
