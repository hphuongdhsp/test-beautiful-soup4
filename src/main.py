"""
@author: Hoang-Phuong
"""

import requests
from bs4 import BeautifulSoup
import os


def CreatFolder(directory: str) -> None:
    """This functuion is to create a directory"""
    if not os.path.exists(directory):
        os.makedirs(directory)


def download_image_2_path(download_link: int, save_path: int) -> None:
    """This function is to downlod the download_link
    and save this file into the save_path
    """
    image_request = requests.get(download_link)
    with open(save_path, "wb") as f:
        f.write(image_request.content)


def examle_get_url_in_tag() ->None:
    from bs4 import BeautifulSoup
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0L1x0DM4mpSt97%2ftYgbxlC2B7n4pvJNhhvRwo8bxiO4B" class="sister" id="link1">Elsie</a>,
    <a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0OPun6GIXb9bh0UOloN9WCYbJtHZQd%2fvB08D2UeudkPP" class="sister" id="link2">Lacie</a> and
    <a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0LirHL60gbBHH3VIishi9CqgtHAKmbGoKNvFheNkumnh" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

    for a in soup.find_all('a', href=True):
        print ("Found the URL:", a['href'])

def examle_get_text_in_tag() ->None:
    from bs4 import BeautifulSoup
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0L1x0DM4mpSt97%2ftYgbxlC2B7n4pvJNhhvRwo8bxiO4B" class="sister" id="link1">Elsie</a>,
    <a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0OPun6GIXb9bh0UOloN9WCYbJtHZQd%2fvB08D2UeudkPP" class="sister" id="link2">Lacie</a> and
    <a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0LirHL60gbBHH3VIishi9CqgtHAKmbGoKNvFheNkumnh" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

    for a in soup.find_all('a', href=True):
        print ("Found the URL:", a.text.strip())

def main()->None:

    web_url = "http://www.globalskinatlas.com/diagindex.cfm/"

    path = "/home/aime/Documents/Phuong/Crawling_image/"
    CreatFolder(path)
    first_request = requests.get(web_url)
    first_soup = BeautifulSoup(first_request.content, "html.parser")

    first_links = first_soup.findAll("a")

    for _, first_link in enumerate(first_links):
        ## add this link to ignore the error
        try:
            ## add this feature, to make sure that we only create the disease folder
            if "diagdetail.cfm?id" in first_link.get("href"):
                link_disease = first_link.get("href")
                disease_name = first_link.text.strip()
                # create disease folder
                CreatFolder(path + disease_name)
                # get request, soup, and all "a" links
                second_request = requests.get("http://www.globalskinatlas.com/" + link_disease)
                second_soup = BeautifulSoup(second_request.content, "html.parser")
                second_links = second_soup.findAll("a")
                # use loop to filter good link to download
                for _, second_link in enumerate(second_links):
                    href_second_link = second_link.get("href")
                    # find the link to can access by clinking "View"
                    if "imagedetail" in href_second_link and second_link.text == "View":
                        link_to_disease = href_second_link
                        # get request, soup, and all "a" links ofthe link from the View clinking
                        third_request = requests.get("http://www.globalskinatlas.com/" + link_to_disease)
                        third_soup = BeautifulSoup(third_request.content, "html.parser")
                        third_links = third_soup.findAll("a")
                        # use loop to filter good link to download
                        for _, third_link in enumerate(third_links):
                            if third_link.get("href") is not None:
                                href_third_link = third_link.get("href")
                                ## if the link have the "View Full Size", we will download directly
                                if third_link.text == "View Full Size":
                                    download_link = href_third_link
                                    # get the file name (abc.jpg)
                                    file_name = download_link.rpartition("/")[-1]
                                    save_path = path + disease_name + "/" + file_name
                                    # download image from the link to save_path
                                    download_image_2_path(download_link, save_path)
                                ## if not, we will click to the image and do the same way as the previous
                                elif "imagedetail" in href_third_link:
                                    link_to_acess_big_image = href_third_link
                                    fourth_request = requests.get(
                                        "http://www.globalskinatlas.com/" + link_to_acess_big_image
                                    )
                                    fourth_soup = BeautifulSoup(fourth_request.content, "html.parser")
                                    fourth_links = fourth_soup.findAll("a")
                                    for _, fourth_link in enumerate(fourth_links):
                                        if fourth_link.text == "View Full Size":
                                            download_link = fourth_link.get("href")
                                            # get the file name (abc.jpg)
                                            file_name = download_link.rpartition("/")[-1]
                                            save_path = path + disease_name + "/" + file_name
                                            # download image from the link to save_path
                                            download_image_2_path(download_link, save_path)

        except Exception as e:
            print(first_link)

if __name__ == "__main__":
    ## example of geting url in a tag in the soup 
    examle_get_url_in_tag()
    ## example of geting text in a tag in the soup 
    examle_get_text_in_tag()
    ## craping web
    main()
