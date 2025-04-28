import requests
from bs4 import BeautifulSoup
import pandas as pd


def parse_imdb_top200():
    url = "https://www.imdb.com/chart/top/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        print("Получаем IMDb Top 200...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        movies = soup.select('li.ipc-metadata-list-summary-item')

        top200 = []
        for movie in movies[:200]:
            title = movie.select_one('h3.ipc-title__text').get_text(strip=True).split('. ')[1]
            year = movie.select_one('span.cli-title-metadata-item').get_text(strip=True)
            rating = movie.select_one('span.ipc-rating-star').get_text(strip=True).split()[0]

            top200.append({
                'Title': title,
                'Year': year,
                'Rating': rating,
                'Position': len(top200) + 1
            })

        df = pd.DataFrame(top200)
        df.to_excel('imdb_top200.xlsx', index=False)

        print("\nПервые 10 фильмов из IMDb Top 250:")
        print(df.head(10))

        return df

    except Exception as e:
        print(f"Ошибка: {e}")
        return None


if __name__ == "__main__":
    parse_imdb_top200()