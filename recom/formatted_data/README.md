## Overview

Files in this folder are modified data from original `movie_lens_data`. We added some features (directors, actors, and IMDB rating) from http://www.omdbapi.com for each movie. Each file has different purpose:

- `data_train_111.csv`: rated movies by user `111` before 2017. It consists of:
    - `userId`: Id of user who rated a movie (111)
    - `userRating`: User rating of a movie, from 0 (bad) to 5 (good).
    - `imdbId`: IMDB ID of a movie
    - `title`: Movie's title
    - `genres`: Movie's genre, if it has multiple genres, it separated with `|`
    - `directors`: Movie's director, if it has multiple directors, it separated with `|`
    - `actors`: Movie's actor, if it has multiple actors, it separated with `|`
    - `imdbRating`: IMDB rating of a movie, from 1 (bad) to 10 (good)
- `data_test_111.csv`: rated movies by user `111` between 2017 and 2018. it has the same format as `data_train_111.csv`.
- `movies1718_all.csv`: list of all movies that release between 2017 and 2018 and exist (rated) on `movie_lens_data`