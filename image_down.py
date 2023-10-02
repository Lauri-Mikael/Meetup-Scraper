import requests
import os

def image_down(url, number, city):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status code is not 200

        image_data = response.content

        os.makedirs(city, exist_ok=True)

        location = f'{city}_image_{number}.jpg'
        location = location.replace(" ", "_")
        location = location.replace(",", "")



        with open(f'{city}/{location}', 'wb') as f:
            f.write(image_data)

    except requests.exceptions.RequestException as e:
        # print(f"An error occurred while downloading the image: {e}")
        return 0

    except IOError as e:
        # print(f"An error occurred while writing the image file: {e}")
        return 0

    except Exception as e:
        # print(f"An unexpected error occurred: {e}")
        return 0

    return location
