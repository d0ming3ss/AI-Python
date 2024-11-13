# Aplikacja do generowania HTML z artykułem i obrazkami

## Opis
Aplikacja jest napisana w Pythonie i służy do generowania kodu HTML na podstawie pliku tekstowego. Zawiera następujące funkcjonalności:

1. Łączy się z API OpenAI.
2. Odczytuje plik tekstowy z treścią artykułu.
3. Przesyła artykuł do OpenAI w celu obróbki. 
4. Wstawia obrazy w odpowiednich miejscach, używając tagów `<img>`. Obrazki są umieszczone pod tekstem, do którego się odnoszą.
5. Dodaje odpowiednie atrybuty `alt` do obrazów, które zawierają dokładny prompt opisujący obraz.
6. Generuje kod HTML bez CSS i JavaScript, zgodnie z wymaganiami.
7. Zapisuje wygenerowany kod HTML do pliku `artykul.html`.

## Funkcjonalności

- **Wstawianie obrazów**: Obrazki są umieszczane w odpowiednich miejscach w artykule i umieszczane pod tekstem.
- **Wygenerowany kod HTML**: Aplikacja generuje kod HTML, który może być bezpośrednio wykorzystany na stronach internetowych. Kod nie zawiera żadnych znaczników `<html>`, `<head>`, ani `<body>`, ponieważ jest przeznaczony tylko do wstawienia w sekcję `<body>` istniejącego dokumentu HTML.
- **Brak CSS i JavaScript**: Wygenerowany HTML nie zawiera żadnego kodu CSS ani JavaScript, co umożliwia łatwe osadzenie go w istniejących projektach.

## Instrukcja uruchomienia

1. **Wymagania wstępne**:
    - Python 3.6 lub wyższy
    - Zainstalowane biblioteki:
      - `openai`
      - `os`

2. **Konfiguracja środowiska**:
    - Ustaw swój klucz API OpenAI w zmiennej środowiskowej `OPENAI_API_KEY`:
    ```bash
    export OPENAI_API_KEY="twój-klucz-API"
    ```

3. **Instalacja zależności**:
    - Zainstaluj bibliotekę OpenAI:
    ```bash
    pip install openai
    ```

4. **Sprawdzenie wersji openai**:
   - Po zainstalowaniu bilbioteki OpenAI, powinno zainstalować najnowszą werjsę - `Version: 1.54.4`
   - Użyj komendy, by sprawdzić swoją werjse openai:
   ```bash
   pip show openai
   ```

5. **Brak najnowszej wersji openai**:
   - Jeśli masz starszą werjsę biblioteki OpenAI, wykonaj tą komendę:
   ```
   pip install --upgrade openai
   ```

6. **Uruchomienie aplikacji**:
    - Wykonaj skrypt Python, aby wygenerować HTML:
    ```bash
    python main.py
    ```
    - Aplikacja odczyta plik `input.txt`, wygeneruje odpowiedni kod HTML i zapisze go w pliku `artykul.html`.

7. **Plik wejściowy**:
    - Plik `input.txt` powinien zawierać treść artykułu, który ma zostać przetworzony.

8. **Wynik**:
    - Plik `artykul.html` będzie zawierał wygenerowany kod HTML przez AI z obrazkami oraz promptami do wygenerowania obrazków pod dany akapit tekstu.

9. **Szablon.HTML**:
    - Do aplikacji dołączono także plik `szablon.html`, który zawiera szablon, w którym użytkownicy mogą wklejać wygenerowaną treść artykułu. Szablon ten umożliwia łatwe wstawienie artykułu do ładnie sformatowanej strony HTML.

10. **Podgląd.HTML**:
   - Plik `podglad.html` to przykład strony, na której użytkownik może zobaczyć podgląd wygenerowanego artykułu w ładnej formie.
