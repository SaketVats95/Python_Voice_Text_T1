import webbrowser

serch_domain = input().lower()
search_string = input()
if serch_domain == "youtube":
    webbrowser.open(
        'https://www.youtube.com/results?search_query='+search_string, new=0)
if serch_domain == "google":
    webbrowser.open("https://www.google.com/search?q="+search_string, new=0)
