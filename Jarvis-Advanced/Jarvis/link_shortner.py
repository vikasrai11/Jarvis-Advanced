import pyshorteners
def shorten_link(original_link):
    
    try:
        shortener=pyshorteners.Shortener()
        short_link=shortener.tinyurl.short(original_link)
        print(short_link)
        return(short_link)
    except Exception as e:
        print("Error while shortening link:{e}") 
           
