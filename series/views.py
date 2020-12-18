from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg

# Create your views here.
def home1(request):
     query = request.GET.get("title")
     allSeries = None
     if query:
          allSeries = Series.objects.filter(name__icontains=query)
     else:
          allSeries = Series.objects.all()
   
     context = {
          "series": allSeries,
     }
     
     return render(request, 'series/index1.html', context)

     #details page
def detail(request, id):
     series = Series.objects.get(id=id)
     reviews = Reviews.objects.filter(series=id).order_by("-comment")

     average = reviews.aggregate(Avg("rating"))["rating__avg"]
     if average == None:
          average = 0
     average = round(average, 1)

     context = {
               "series":series,
               "reviews": reviews,
               "average": average
     }
     return render(request, 'series/details1.html', context)

#add series to  the database

def add_series(request):
     if request.user.is_authenticated:
          if request.user.is_superuser:
               if request.method == "POST":
                   form = SeriesForm(request.POST or None)
          
                   #check if the form is valid 
          
                   if form.is_valid():
                       data = form.save(commit=False)
                       data.save()
                       return redirect("series:home1")
               else:
                  form = SeriesForm()
               return render(request, 'series/addseries.html', {"form": form, "controller": "Add series"}) 
     

          #if they are not admin
          return redirect("series:home1")
     #if they are not logged in
     return redirect("accounts:login")

#edit the movies 

def edit_series(request, id):
     if request.user.is_authenticated:
          if request.user.is_superuser:     
              #get the movies linked with id 
      
              series= Series.objects.get(id=id)

              #form check 
      
              if request.method == "POST":
                  form = SeriesForm(request.POST or None, instance=series)

                  #check if the for is valid 
           
                  if form.is_valid():
                      data = form.save(commit=False)
                      data.save()
                      return redirect("series:detail", id)
              else:
                  form = SeriesForm(instance=series) 
          
              return render(request, 'series/addseries.html', {"form": form, "controller": "Edit Series"})
     
          #if they are not admin
          return redirect("series:home1`")
     #if they are not logged in
     return redirect("accounts:login")     

#delete movies

def delete_series(request, id):
     if request.user.is_authenticated:
          if request.user.is_superuser:     
     
              #get the movie

     
              series= Series.objects.get(id=id)

              #delete the movie

              series.delete()
              return redirect("series:home1")
          #if they are not admin
          return redirect("series:home1")
     #if they are not logged in
     return redirect("accounts:login")

#add review



def add_review(request, id):
     if request.user.is_authenticated:
          series = Series.objects.get(id=id)
          if request.method == "POST":
               form = ReviewForm(request.POST or None)
               if form.is_valid():
                   data = form.save(commit=False)
                   data.comment = request.POST["comment"]
                   data.rating = request.POST["rating"]
                   data.user = request.user
                   data.series = series
                   data.save()
                   return redirect("series:detail", id)
          else:
              form = ReviewForm()
          return render(request, 'series/details1.html', {"form": form})
     else:
         return redirect("accounts:login")

    #edit the review
     
def edit_review(request, series_id, review_id):
     if request.user.is_authenticated:
         series = Series.objects.get(id=series_id)
         #review
         review = Reviews.objects.get(series=series, id=review_id)

         #check if the review was done by the logged in user
         if request.user == review.user:
              #grant permission 
               if request.method == "POST":
                   form = ReviewForm(request.POST, instance=review)  
                   if form.is_valid():
                       data = form.save(commit=False)
                       if (data.rating > 10) or (data.rating < 0):
                            error = "Out of range. Please select rating from 0 to 10."
                            return render(request, 'series/editreview1.html', {"error": error, "form": form})
                       else:
                            data.save()
                            return redirect("series:detail", series_id)
               else:
                    form = ReviewForm(instance=review)
               return render(request, 'series/editreview1.html', {"form": form})                
         else:
               return redirect("series:detail", series_id)
     else:
          return redirect("accounts:login")

# delete review

def delete_review(request, series_id, review_id):
     if request.user.is_authenticated:
         series = Series.objects.get(id=series_id)
         #review
         review = Reviews.objects.get(series=series, id=review_id)

         #check if the review was done by the logged in user
         if request.user == review.user:
              #grant permission to delete review
              review.delete()
         
         return redirect("series:detail", series_id)
    
     else:
          return redirect("accounts:login")          
         
         
          #contact us page

def contact(request):
     context = {
          "contacts": contact,
     }
     return render(request, 'main/contact.html', context)
