from flask import Flask,render_template
#import news api 
from newsapi import NewsApiClient
#create name and run
app = Flask(__name__, template_folder='./template/')
 

#create home route
@app.route('/')
def index():
    #init the api and top headlines for news
    newsapi = NewsApiClient(api_key='49ac8a649aed4ec69481c89777f257c0')
    topHeadlines = newsapi.get_top_headlines(sources='bbc-news')
    
    #take the article 
    articles = topHeadlines['articles']
    
    #now get description, news, img
    desc = []
    news = []
    img  = []
    content = []
    publish = []
    
    
    #now take img and articles one by one
    for i in range(len(articles)):
        myarticles = articles[i]
        #now get this in news list
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        publish.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
        
        
        
    #now get all this news in context 
    myContext = zip(news, desc, img)   
        
        
    
    return render_template('index.html', context=myContext)
    
#make a new url for alzariah news 
@app.route('/alzazirah-news')
def alzazirah():
    newsapi = NewsApiClient(api_key='49ac8a649aed4ec69481c89777f257c0')
    topHeadlines = newsapi.get_top_headlines(sources='al-jazeera-english')
    
    #take the article 
    articles = topHeadlines['articles']
    
    #now get description, news, img
    desc = []
    news = []
    img  = []
    content = []
    publish = []
    
    
    #now take img and articles one by one
    for i in range(len(articles)):
        myarticles = articles[i]
        #now get this in news list
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        publish.append(myarticles['publishedAt'])
        content.append(myarticles['content'])
        
        
        
    #now get all this news in context 
    myContext = zip(news, desc, img)   
        
        
    
    return render_template('alzazirah.html', context=myContext)
    

#run the app 
if __name__ == '__main__':
    app.run(debug=True)
    