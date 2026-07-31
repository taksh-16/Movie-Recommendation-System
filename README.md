## Dataset

For this project, I used a custom movie dataset named **`movie_data.csv`**. The dataset contains movie titles along with a **tags** column, which is used to generate content-based recommendations.

This dataset was prepared after following the movie recommendation system lecture. During the lecture, movie information such as title, genres, keywords, cast, crew, and overview was collected from the **TMDB (The Movie Database) API**. These features were then combined into a single **tags** column, resulting in the final dataset used in this project.

Columns used in this project:
- **movie_title** – Name of the movie
- **tags** – Combined text containing important information about the movie, used for generating recommendations