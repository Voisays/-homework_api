import requests

def main():
    # Отправляем GET-запрос к публичному API
    url = "https://jsonplaceholder.typicode.com/posts"
    print(f"Отправляем запрос к {url}...")

    try:
        response = requests.get(url)

        # Проверяем, что запрос прошёл успешно (статус 200)
        if response.status_code == 200:
            posts = response.json()

            print("\n--- Первые 5 постов ---\n")

            # Берем первые 5 элементов из списка
            for post in posts[:5]:
                print(f"Заголовок: {post['title']}")
                print(f"Тело: {post['body']}")
                print("-" * 40)
        else:
            print(f"Ошибка! Сервер вернул код: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при подключении: {e}")

if __name__ == "__main__":
    main()