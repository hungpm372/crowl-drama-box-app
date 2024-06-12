import requests
import os


def download_file(url, i):
    os.makedirs('data', exist_ok=True)

    resolution = '540p' if '540p' in url else '720p' if '720p' in url else ''

    file_name = os.path.join('data', f"EP_{i}_{resolution}.mp4")

    try:
        response = requests.get(url, stream=True)
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)
        print(f"File saved as {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {str(e)}")


def download_urls_from_content():
    try:
        with open('out_put.txt', 'r') as file:
            i = 1
            j = 1
            for line in file:
                if j == 3:
                    i += 1
                    j = 1
                line = line.strip()
                download_file(line, i)
                j += 1

    except Exception as e:
        print(f"Error processing content: {str(e)}")


download_urls_from_content()
