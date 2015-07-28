__author__ = 'Admin'

import urllib2
import BeautifulSoup
import csv

PAGE_URL = "https://www.upwork.com/o/jobs/browse/" # page for parsing


def get_html(url):
    response = urllib2.urlopen(url)
    return response.read()

def search(text):
    #text = text1.encode('ascii')
    #print dir(text)
    return text.find('Python') > -1  \
           or text.find('Django') > -1\
           or text.find('PyQt') > -1\
           or text.find('Android') > 0\
           or text.find('Java') > -1\
           or text.find('Unity3D') > -1\
           or text.find('Developer') > -1\
           or text.find('Ptoject') > -1\
           or text.find('Web') > -1



def parse(html):
    soup = BeautifulSoup.BeautifulSoup(html)
    section = soup.find('section','js-search-results air-card m-xs-top')
    #print article
    list1 = []
    for item in section.findAll('article'):
        header = item.findAll('header')
        #if (header[0].a.text.find('Python') > -1) or \
         #       (header[0].a.text.find('python') > -1):
        if search(header[0].a.text):
            list1.append({
                'title': header[0].a.text
         })
    return list1


def get_pages(html):
    soup = BeautifulSoup.BeautifulSoup(html)
    pages = soup.find('ul','pagination')
    a = pages.findAll('a')[-2].text
    return int(a)

def csv_writer(projects,path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow('Interesting  Projects')

        print dir(writer)
        for i in projects:
            writer.writerow(i['title'])



def main():
    dates = []
    pages = 50  # parse for first 50 pages
    #pages = get_pages(get_html(PAGE_URL))
    for page in range(1,pages+1):
        dates.extend(parse(get_html(PAGE_URL + '?page=%d' % page)))

    for item in dates:
        print item
    #print dir(BeautifulSoup.BeautifulSoup)

    csv_writer(dates,'interesting_projects.csv')
main()