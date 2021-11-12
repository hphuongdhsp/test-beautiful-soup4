# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 14:47:39 2021

@author: Du
"""

import requests
from bs4 import BeautifulSoup
import os
import tqdm
import urllib.request


def CreatFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Successfully created the directory %s " % directory)


web_url = "http://www.globalskinatlas.com/diagindex.cfm"
path = "/Users/nguyenphuong/Desktop/globalskinatlas"

CreatFolder(path)

r = requests.get(web_url)
soup = BeautifulSoup(r.content, "html.parser")


## get all tag <a>
link_a = soup.find_all("a")

for link in link_a:
    # get href in the link
    link_href = link.get("href")
    # if "diagdetail.cfm?id" in the href link, then we get the text (disease name)
    if "diagdetail.cfm?id" in link_href:
        ## get the disease_name
        disease_name = link.text
        ## make the disease folder = path + disease_name
        disease_path = os.path.join(path, disease_name)
        ## mkdir disease_path
        CreatFolder(disease_path)
        ###### This part we will clink on the new website ###

        ## the same idea, we will get request and soup
        sub_r = requests.get(os.path.join("http://www.globalskinatlas.com", link_href))
        sub_soup = BeautifulSoup(sub_r.content, "html.parser")
        ## get all tag <a>
        sub_link_a = sub_soup.find_all("a")
        for sub_link in sub_link_a:
            sub_link_href = sub_link.get("href")
            if "imagedetail" in sub_link_href and sub_link.text == "View":
                sub_sub_r = requests.get(
                    os.path.join("http://www.globalskinatlas.com", sub_link_href)
                )
                sub_sub_soup = BeautifulSoup(sub_sub_r.content, "html.parser")

                ## Download small images

                # img_urls = sub_sub_soup.findAll("img")
                # for img_url in img_urls:
                #     img_url_src = img_url.get("src")
                #     if "http://www.globalskinatlas.com/upload" in img_url_src:
                #         destination = os.path.join(disease_path, "small")
                #         CreatFolder(destination)
                #         file_name = img_url_src.rpartition("/")[-1]
                #         path_save = os.path.join(destination, file_name)
                #         urllib.request.urlretrieve(img_url_src, path_save)

                ## This part is to download the big image when we open the link
                for img_url in sub_sub_soup.findAll("a", href=True):
                    if img_url.text == "View Full Size":
                        img_url_src = img_url.get("href")
                        file_name = img_url_src.rpartition("/")[-1]
                        path_save = os.path.join(disease_path, file_name)
                        urllib.request.urlretrieve(img_url_src, path_save)
                    if "imagedetail" in img_url.get("href"):
                        r3 = requests.get(
                            os.path.join(
                                "http://www.globalskinatlas.com", img_url.get("href")
                            )
                        )
                        soup3 = BeautifulSoup(r3.content, "html.parser")
                        for img_url_3 in soup3.findAll("a", href=True, target="_blank"):
                            if img_url.text == "View Full Size":
                                img_url_src_3 = img_url.get("href")
                                file_name_3 = img_url_src.rpartition("/")[-1]
                                path_save_3 = os.path.join(disease_path, file_name_3)
                                urllib.request.urlretrieve(img_url_src, path_save_3)

