# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:51:20 2017

@author: ahorn
"""
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
#toy_story.show_trailer()

crossroads = media.Movie("Crossroads",
                        "A story of a blues boy from Long Island",
                        "https://upload.wikimedia.org/wikipedia/en/d/d8/Crossroadsposter1986.jpg",
                        "https://www.youtube.com/watch?v=bMAkr_Z74E8")

#fugitive:
fugitive = media.Movie("The Fugitive",
                        "A man on the run.",
                        "https://upload.wikimedia.org/wikipedia/en/c/c7/The_Fugitive_movie.jpg",
                        "https://www.youtube.com/watch?v=GoyqZJWjOjU")




#star wars
star_wars = media.Movie("Star Wars IV",
                        "Sci-Fi thriller.",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")




#Rocky:
rocky = media.Movie("Rocky I",
                        "Rocky Balboa",
                        "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
                        "https://www.youtube.com/watch?v=3VUblDwa648")



movies = [toy_story,crossroads,fugitive,star_wars,rocky]
fresh_tomatoes.open_movies_page(movies)
