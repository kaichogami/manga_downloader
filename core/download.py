"""This is used to download files or images and store in a directory given by 
   the manga name.
"""

import os, urllib2, spell


class download:

    def __init__(self, comic_name, start_chap, end_chap):
        #check if the spelling of manga is right

        s = spell.spell(comic_name.replace('_', ' '))

        self.comic_name = s.correct()
        self.start_chap = start_chap
        self.end_chap = end_chap
        self.current_chap = start_chap

        self.base_url = 'http://www.mangapanda.com/'
        
        #create a new directory
        if not os.path.exists('download/'+self.comic_name): os.makedirs('download/'+self.comic_name)

        #change cwd to path
        os.chdir('download/'+self.comic_name)
        self.comic_path = self.comic_name.replace(' ', '-')

        
    def download_chap(self, chap):
        #download image of a chapter by finding the first
        #.jpg link in the html page. If anything goes wrong, error
        #should be in .jpg finding logic
        if not os.path.exists(str(chap)): os.makedirs(str(chap))
        current_page = 1

        while True:
            #try downloading the page if exists
            #else we know we reached the end of chapter, hence end
            try:

                response = urllib2.urlopen(self.base_url+self.comic_path+'/'+str(chap)+'/'+str(current_page))

            except urllib2.HTTPError as e:
                print('Downloaded chapter {0}'.format(chap))
                return True

            html = response.read()
            print('read page')

            #this logic will work for only Mangapanda
            #return False if last chapter is read
            if html.find('Related_Mangas') != -1:
                return False

            #find .jpg location
            jpg = html.find('.jpg')

            #find http location linked to .jpg
            http = html[jpg-100:jpg]
            http = http.find('http')


            link = html[jpg - (100 - http) :jpg+4]     #+4 to link till the end of .jpg

            #download it
            print("Downloading page {0}".format(current_page))

            opener = urllib2.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]
            res = opener.open(link)
            data = res.read()
            f = open(str(chap)+'/'+str(current_page),'w')
            print('saved the image')
            f.write(data)
            f.close()
            print("downloaded page {0}".format(current_page))
                
            #change the current page
            current_page+=1


    def start_download(self):
        current = int(self.start_chap)

        while current <= int(self.end_chap):
            self.download_chap(str(current))
            current+=1

        return            

if __name__ == '__main__':
    

    d = download('fairyy tail', 5,6)
    d.start_download()
