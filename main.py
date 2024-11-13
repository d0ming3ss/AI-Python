import os
from openai import OpenAI

# Ustawienie klucza API
os.environ["OPENAI_API_KEY"] = "your_API_key"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_article(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def generate_html(article_content):
    # Przygotowanie promptu
    prompt = (f"Stwórz HTML dla artykułu poniżej, "
              f"wstawiając obrazy w odpowiednich miejscach z tagami <img src='image_placeholder.jpg' alt='prompt opisu'> "
              f"i użyj tytułów pod obrazami. Każdy obrazek powinien mieć alt z dokładnym promptem dla obrazu.\n"
              f"Zwróć tylko zawartość HTML do wstawienia pomiędzy tagami <body> i </body>, "
              f"nie dołączaj żadnych znaczników <html>, <head>, ani <body>, "
              f"oraz nie używaj żadnego kodu CSS ani JavaScript. Kod HTML nie powinien zawierać niczego poza "
              f"zawartością do wstawienia w <body>.\n\n{article_content}")
    
    # Wywołanie OpenAI API z modelem gpt-4
    response = client.chat.completions.create(
        model="gpt-4",  
        messages=[{"role": "system", "content": "You are a helpful assistant that creates HTML code."},
                  {"role": "user", "content": prompt}],
        max_tokens=1500,
        temperature=0.7,
    )
    
    return response.choices[0].message.content.strip()

def save_html(filename, html_content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    article = read_article("input.txt")
    html_content = generate_html(article)
    save_html("artykul.html", html_content)
