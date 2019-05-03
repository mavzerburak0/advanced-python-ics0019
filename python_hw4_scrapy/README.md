## Web crawler

### This small project is written by Kadir Burak Mavzer for Advanced Python (ICS0009) course at IT College of Taltech.

Scrapy library is used to achieve the requirements.

You can run the project by navigating to the project directory in your terminal and typing:

    scrapy crawl products -o products.json
    
This command will crawl the url: 

    https://ordi.eu/lauaarvutid#

and generate a <i>products.json</i> file filled with name, price and image link information related to the products listed.

###### NB! If you run the same command twice in a row, it will break your .json file. Therefore, either change the name of the output file, delete the previous file created or erase the result of the first run.

It follows pagination links on the same domain as well so you don't have to change the url every time you run the program to get the products on different pages.

Scrapy documentation link: 

    https://docs.scrapy.org/en/latest/

