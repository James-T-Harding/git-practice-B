select distinct title
from movies
inner join ratings on movie_id = movies.id
where rating >= 4;