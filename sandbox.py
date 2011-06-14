from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
    '''
    def handle_starttag(self, *args):
        print("handle_starttag%s called." % str(args))

    def handle_startendtag(self, *args):
        print("handle_startendtag%s called." % str(args))

    def handle_endtag(self, *args):
        print("handle_endtag%s called." % str(args))

    def handle_data(self, *args):
        print("handle_data%s called." % str(args))

    def handle_charref(self, *args):
        print("handle_charref%s called." % str(args))

    def handle_entityref(self, *args):
        print("handle_entityref%s called." % str(args))

    def handle_comment(self, *args):
        print("handle_comment%s called." % str(args))

    def handle_decl(self, *args):
        print("handle_decl%s called." % str(args))

    def handle_pi(self, *args):
        print("handle_pi%s called." % str(args))
    '''        
    def handle_li(self, *args):
        print("handle_li%s called." % str(args))

#sock = urllib.request.urlopen("http://diveintopython.org/") 
sock = urllib.request.urlopen("http://www.bbc.co.uk/radio1/chart/singles") 
htmlSource = sock.read().decode("utf8")

print(htmlSource)

theParser = MyHTMLParser()
theParser.feed(htmlSource)
theParser.close()
