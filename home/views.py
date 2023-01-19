from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from django.http import HttpResponse


TMDB_API_KEY = "c8793e8100a999a9b60b1647fe45ba1c"
# Create your views here.
def search(request):
    
    # Get the query from the search box
    query = request.GET.get('q')
    data = request.GET.get("data")
    
    print(data)
    
    results=[]
    
    
    if query:
        
        data = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=ko-KR&page=1&include_adult=false&query={query}")
        print(data.json())
       # temp=[]
       # for n in data.json()["results"]:
       #     if len(temp)<3:
       #         temp.append({"name": n["name"],"poster":n["poster_path"],"overview":n["overview"]})
       #     else:
       #         results.append(temp)
       #         temp.append({"name": n["name"],"poster":n["poster_path"],"overview":n["overview"]})
       #     
       # results.append(temp) if len(temp) > 0 else None
    else:
        return HttpResponse("Please enter a search query")
    
    if data == "json":
        return JsonResponse(data.json())
    
    return render(request, 'home/results.html', {
        "q":query,
        "data" : data.json(),
    })

    
def index(request):
    return render(request, 'home/index.html')

def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR")
    
    provider = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers?api_key={TMDB_API_KEY}&language=ko-KR&page=1")
    
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={TMDB_API_KEY}&language=ko-KR&page=1")
    return render(request, "home/movie_detail.html",{
        "data": data.json(),
        "recommendations":recommendations.json(),
        
    })
    
def view_trendings_results(request):
    time_window = request.GET.get("time_window")
    
    trendings = requests.get(f"https://api.themoviedb.org/3/trending/movie/{time_window}?api_key={TMDB_API_KEY}&language=ko-KR")
    return JsonResponse(trendings.json())
