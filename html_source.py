from urllib import urlopen, urlretrieve

urladdr = 'https://www.google.com'

def print_html(urladdr):
    webpage = urlopen(urladdr)
    html = webpage.read()
    print html

print_html(urladdr)

def save_html(urladdr, localfile):
    urlretrieve(urladdr, localfile)

save_html(urladdr, r'C:\Users\Tanwir\Desktop\Python Lecture 11\index.html')
    
