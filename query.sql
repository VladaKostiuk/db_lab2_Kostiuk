-- query 1
SELECT years.year_value, count(years.year_value) FROM 
films INNER JOIN years ON films.year_id = years.year_id
GROUP BY years.year_value


-- query 2
SELECT genres.genre_name, count(genres.genre_name) FROM
genres INNER JOIN films ON genres.genre_id = films.genre_id
GROUP BY genres.genre_name


-- query 3
SELECT directors.director_name, count(directors.director_name) FROM 
films INNER JOIN directors ON films.director_id = directors.director_id
GROUP BY directors.director_name