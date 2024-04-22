import gdown
import zipfile
import os
import shutil
from dotenv import load_dotenv
import argparse

load_dotenv()

def download_and_extract(url, destination):
    gdown.download(f"https://drive.google.com/uc?id={url}", destination, quiet=False)

    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(destination))
    os.remove(destination)

if __name__ == "__main__":
    path = os.getenv('PATH_DATASET')
    if not os.path.exists(path):
        os.makedirs(path)

    file_urls = {
        '1': os.getenv("FILE_URL1_ID"),
        '2': os.getenv("FILE_URL2_ID"),
        '3': os.getenv("FILE_URL3_ID")
    }

    parser = argparse.ArgumentParser(description='Download and extract ZIP file from Google Drive.')
    parser.add_argument('options', 
                        help='Select one or more options for the URLs (e.g., "12" or "3"). \n'
                            '1: corresponds to the ini dataset \n'
                            '2: corresponds to the pyronear dataset \n'
                            '3: corresponds to the total FP dataset', 
                    type=str)

    args = parser.parse_args()

    selected_options = args.options

    for option in selected_options:
        url_id = file_urls.get(option)
        if url_id:
            destination = os.path.join(path, f'file_{url_id}.zip')
            download_and_extract(url_id, destination)
        else:
            print(f"Invalid option '{option}'.")

    print("Download and extraction completed.")