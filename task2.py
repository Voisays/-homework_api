import requests

def main():
    city = input("Введите название города (например, Moscow): ")

    # Формируем URL. format=j1 означает, что мы хотим ответ в JSON
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)

        # Проверяем, что запрос успешен
        if response.status_code == 200:
            data = response.json()

            # Достаем текущую погоду из ответа
            current = data['current_condition'][0]

            temperature = current['temp_C']
            # Описание погоды лежит в списке, берем первый элемент
            weather_desc = current['weatherDesc'][0]['value']

            print("\n--- Погода ---")
            print(f"Город: {city}")
            print(f"Температура: {temperature} °C")
            print(f"Описание: {weather_desc}")

        else:
            print(f"Ошибка. Код ответа: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
    except KeyError:
        print("Не удалось найти город. Проверьте название.")

if __name__ == "__main__":
    main()