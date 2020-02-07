#import packages
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

rankingls=[]
namels=[]
ratingls=[]
reviewls=[]
phonels=[]
addressls=[]
districtls=[]


#the url you want crawl
head='https://www.yelp.com/search?find_desc=icecream&find_loc=10023'
ai='&start='
for i in range(0,99,10):
    url=head+ai+str(i)
    #print(url)
    #use urllib2 module to open the url
    ourUrl=urllib.request.urlopen(url)

    soup=BeautifulSoup(ourUrl,'html.parser')
    #create a BeautifulSoup object, which represents the document as a nested data structure
    #parse the page

    # to see what inside the soup
    #print(soup.prettify())


    for i in soup.find_all('div',{'class':'lemon--div__373c0__1mboc largerScrollablePhotos__373c0__3FEIJ arrange__373c0__UHqhV border-color--default__373c0__2oFDT'}):
        rankingname=i.find('div',{'class':'lemon--div__373c0__1mboc businessNameWithNoVerifiedBadge__373c0__24q4s display--inline-block__373c0__2de_K border-color--default__373c0__2oFDT'})
        ranking=rankingname.find('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--black-regular__373c0__38bRH text-align--left__373c0__2pnx_ text-size--inherit__373c0__2gFQ3'}).contents[0]
        if str(ranking).isdigit():
            left=i.find('div',{'class':'lemon--div__373c0__1mboc mainAttributes__373c0__1r0QA arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT'})
            right=i.find('div',{'class':'lemon--div__373c0__1mboc secondaryAttributes__373c0__7bA0w arrange-unit__373c0__1piwO border-color--default__373c0__2oFDT'})
            name1=rankingname.find('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--black-regular__373c0__38bRH text-align--left__373c0__2pnx_ text-size--inherit__373c0__2gFQ3'})
            name=name1.find('a',{'class':'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'}).contents[0]
            ratingreview=left.find('div',{'class':'lemon--div__373c0__1mboc display--inline-block__373c0__2de_K border-color--default__373c0__2oFDT'})
            try:
                ratingtag=i.find('span',{'class':'lemon--span__373c0__3997G display--inline__373c0__1DbOG border-color--default__373c0__2oFDT'}).contents[0]
                rating=ratingtag.get('aria-label')
            except:rating='None'
            review_tag=ratingreview.find('div',{'class':'lemon--div__373c0__1mboc attribute__373c0__1hPI_ display--inline-block__373c0__2de_K border-color--default__373c0__2oFDT'})
            review=review_tag.find('span',{'class':'lemon--span__373c0__3997G text__373c0__2pB8f reviewCount__373c0__2r4xT text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_'}).contents[0]
            print('Ranking: ',ranking)
            rankingls.append(ranking)
            print('Name: ',name)
            namels.append(name)
            rating=(rating.split())[0]
            print('rating: ',rating)
            ratingls.append(rating)
            print('review: ',review)
            reviewls.append(review)
            phone_tag=right.find('div',{'class':'lemon--div__373c0__1mboc display--inline-block__373c0__2de_K u-space-b1 border-color--default__373c0__2oFDT'})
            phone=phone_tag.find('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'}).getText()
            if not str(phone)[0]=='(':phone='None'
            print('phone',phone)
            phonels.append(phone)
            try:
                address1=right.find('address',{'class':'lemon--address__373c0__2sPac'})
                address=address1.find('span',{'class':'lemon--span__373c0__3997G'}).getText() #needs guardian
            except:
                address='None'
            print('Detailed Address: ',address)
            addressls.append(address)
            district1=i.find('div',{'class':'lemon--div__373c0__1mboc u-space-b1 border-color--default__373c0__2oFDT'})
            district2=district1.find('p',{'class':'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})
            if district2==None: district='None'
            else:district=district2.getText()
            print('District Information: ',district)
            districtls.append(district)
            print('*************************')
            df=pd.DataFrame({'ranking':rankingls,'name':namels,'rating':ratingls,'review':reviewls,'phone':phonels,'address':addressls,'district':districtls})
            df.to_csv("yelp.csv",index=False)
