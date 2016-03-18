#!/usr/bin/bash 
scrapy crawl justia_lawyers_imgpip -o justia_lawyers_imgpip.csv -t csv
mv justia_lawyers_imgpip.csv ..
