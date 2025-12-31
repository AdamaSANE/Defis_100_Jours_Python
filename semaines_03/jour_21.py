# Wikipedia Article Scraper
import requests
from bs4 import BeautifulSoup 

# Step 1: Get the URL of the Wikipedia article
def get_wikipedia_article_url(article_title):
  url = f"https://en.wikipedia.org/wiki/{article_title.replace(' ', '_')}"
  reponse = requests.get(url)
  if reponse.status_code == 200:
    return reponse.text
  else:
    print(f"Failed to retrieve article: {reponse.status_code}. Check the article title and try again.")
    return None

# Step 2: Extract Article Title
def extract_article_title(soup):
  return soup.find('h1').text

# Step 3: Extract Article Summary
def extract_article_summary(soup):
  paragraphs = soup.find_all('p')
  for para in paragraphs:
    if para.text.strip():
      return para.text.strip()
  return "No summary found."

# Step 4: Extract Headings
def extract_headings(soup):
  headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
  return headings

# Step 5: Extract Related Links
def extract_related_links(soup):
  links = []
  for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if href.startswith('/wiki/') and ":" not in href:
      links.append(f"https://en.wikipedia.org{href}")
  return list(set(links))[:5]  # Remove duplicates

# Step 6: Main Program
def main():
  article_title = input("Enter the Wikipedia article title: ").strip()
  page_content = get_wikipedia_article_url(article_title)

  if page_content:
    soup = BeautifulSoup(page_content, 'html.parser')

    title = extract_article_title(soup)
    summary = extract_article_summary(soup)
    headings = extract_headings(soup)
    related_links = extract_related_links(soup)

    print("\n--- Wikipedia Article Information ---\n")
    print(f"\nArticle Title: {title}")
    print(f"\nSummary: {summary}")
    print("\nHeadings:")
    for heading in headings[:5]:  # Display only first 5 headings
      print(f"- {heading}")
    print("\nRelated Links:")
    for link in related_links:
      print(f"- {link}")

# Run the main program
if __name__ == "__main__":
  main()