# product-name
# price-box > price
# product-image

from bs4 import BeautifulSoup
import requests
import json


def get_products(url):
    # all_products is where the product information dicts will be stored
    all_products = []

    page_response = requests.get(url, timeout=5)
    soup = BeautifulSoup(page_response.content, "lxml")

    # col_main prevents other prices on the page to be crawled
    col_main = soup.find_all("div", {"class": "category-products"})

    for tag in col_main:
        product_names = tag.find_all('h2', class_ = 'product-name')
        product_price = tag.find_all('span', class_='price')
        product_img = tag.find_all('img')
        for i in range(len(product_names)):
            product_dict = {"Product name": [product.text for product in product_names][i],
                            "Product price": [price.text for price in product_price][i],
                            "Product image": [image['src'] for image in product_img][i]}

            all_products.append(product_dict)

    # crawling pages with pagination
    try:
        next_page = soup.find("a", class_='next')["href"]
        if next_page:
            get_products(next_page)
    except:
        print("No more pages!")

    # write all products to a .json file
    with open('products.json', 'w') as fout:
        json.dump(all_products, fout)


def main():
    get_products("https://ordi.eu/lauaarvutid")


if __name__ == '__main__':
    main()


