import requests
from django.shortcuts import render

TMDB_API_KEY = "c8793e8100a999a9b60b1647fe45ba1c"

# Create your views here.
def watchlist(request):
    return render(request, "dashboard/watchlist.html")


def Profile(request):
    return render(request, "dashboard/index.html")

def Edit(request):
    provider = requests.get(f"https://api.themoviedb.org/3/watch/providers/movie?api_key={TMDB_API_KEY}&language=eg-EN")
    
    provider_id = [ 8, 192, 337, 356, 97, 119, 350]
    
    
    return render(request, "dashboard/ott.html",{
        "provider":provider.json(),
        "id":provider_id
    })
