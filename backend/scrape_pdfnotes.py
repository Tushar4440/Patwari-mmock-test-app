import requests
from bs4 import BeautifulSoup
import json
import time
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_all_quiz_links(main_url):
    print(f"Fetching main page: {main_url}")
    response = requests.get(main_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    # Find links that point to specific quiz parts
    for a in soup.find_all('a', href=True):
        if 'uttarakhand-gk-online-quiz-' in a['href']:
            links.append(a['href'])
    
    unique_links = list(set(links))
    print(f"Found {len(unique_links)} quiz part links.")
    return unique_links

def scrape_page(url):
    print(f"Scraping: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        page_questions = []

        # Match "Q1.", "Q2.", "Q 1.", "Q.1" etc.
        q_pattern = re.compile(r'^Q\s*\.?\s*\d+\s*\.', re.IGNORECASE)

        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if q_pattern.match(text):
                question_text = re.sub(r'^Q\s*\.?\s*\d+\s*\.\s*', '', text)
                
                # Get Options (usually the next UL or OL)
                options = []
                sibling = p.find_next_sibling()
                if sibling and sibling.name in ['ul', 'ol']:
                    options = [li.get_text().strip() for li in sibling.find_all('li')]
                
                # Get Answer (in Shortcodes Ultimate spoilers)
                correct_answer = ""
                spoiler = p.find_next_sibling('div', class_='su-spoiler')
                if spoiler:
                    content = spoiler.find('div', class_='su-spoiler-content')
                    if content:
                        ans_raw = content.get_text().strip()
                        # Clean "उत्तर- " or "Ans: "
                        correct_answer = re.sub(r'^(उत्तर|Ans|Answer|Ans\.)\s*[:\-]?\s*', '', ans_raw)
                
                if len(options) >= 2:
                    page_questions.append({
                        "section": "Uttarakhand GK",
                        "sub_topic": "General GK",
                        "source": "pdfnotes.co",
                        "text": question_text,
                        "options": options,
                        "correct_answer": correct_answer,
                        "explanation": "विस्तृत व्याख्या उपलब्ध नहीं है।"
                    })
        
        return page_questions
    except Exception as e:
        print(f"Error on {url}: {e}")
        return []

def run_full_scrape():
    main_url = "https://www.pdfnotes.co/uttarakhand-gk-online-quiz-mcq/"
    quiz_links = get_all_quiz_links(main_url)
    
    all_questions = []
    for link in quiz_links:
        questions = scrape_page(link)
        all_questions.extend(questions)
        print(f"Added {len(questions)} questions. Total: {len(all_questions)}")
        time.sleep(1) # Be polite to the server

    print(f"Final Count: {len(all_questions)}")
    with open('scraped_questions.json', 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=4)
    print("Saved to scraped_questions.json")

if __name__ == "__main__":
    run_full_scrape()