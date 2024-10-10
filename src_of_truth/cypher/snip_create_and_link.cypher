MATCH
  (x: animation)
WHERE x.movie_title = 'Kung Fu Panda 2'
CREATE (
 : animation {
  movie_title: 'Kung Fu Panda 3',
  release_year: 2016
 }
)-[: sequel]->(x)