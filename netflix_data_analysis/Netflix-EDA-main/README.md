# Netflix EDA (Exploratory Data Analysis)
![image](https://github.com/AaryanPurohit/Netflix-EDA/assets/112640418/1a960059-3f17-4544-801f-6fa382d45b4f)



## Overview📺🍿

Netflix is one of the most popular media and video streaming platforms. They have over 10000 movies🎥 or # tv shows📺 available on their platform, as of mid-2021, they have over 222M Subscribers globally🌍. This tabular dataset consists of listings of all the movies and tv shows available on Netflix, along with details such as - cast, directors🎬, ratings⭐, release year📅, duration⏱️, etc.

This Python script analyzes Netflix data using the Pandas, Matplotlib, Seaborn, and WordCloud libraries. The dataset used in this analysis contains information about Netflix shows and movies, including details such as title, genre, cast, release date, and more.

**The analysis covers various aspects of the dataset, including data cleaning, exploratory data analysis, and data visualization. It provides insights into the distribution of content, ratings, genres, countries, and other factors within the Netflix library.**

## Prerequisites🛠️

Before running the code, ensure you have the following libraries installed:
- Pandas🐼
- NumPy🧮
- Matplotlib📊
- Seaborn📈
- WordCloud☁️

You can install these libraries using pip:

pip install pandas numpy matplotlib seaborn wordcloud

## Usage🚀
1. Download the Netflix dataset (netflix.csv) and place it in the same directory as the Python script.

2. Open the Python script in a suitable environment (e.g., Jupyter Notebook or any Python IDE).

3. Run the script. It will load and analyze the Netflix data, generating various visualizations and insights.

4. Explore the generated plots and insights to gain a better understanding of the Netflix dataset.

## Files📁
netflix.csv: The dataset containing Netflix show and movie information.
Netflix_Data_Analysis.ipynb: The Python script for data analysis.

## Understanding the Dataset📊

The dataset has a list of all the TV shows/movies available on Netflix:
1. **Show_id**: Unique ID for every Movie / Tv Show
2. **Type**: Identifier - A Movie or TV Show
3. **Title**: Title of the Movie / Tv Show
4. **Director**: Director of the Movie
5. **Cast**: Actors involved in the movie/show
6. **Country**: Country where the movie/show was produced
7. **Date_added**: Date it was added on Netflix
8. **Release_year**: Actual Release year of the movie/show
9. **Rating**: Maturity Rating of the movie/show
10. **Duration**: Total Duration - in minutes or number of seasons
11. **Listed_in**: Genre
12. **Description**: The summary description

## Results📊
The analysis provides insights into the Netflix dataset, including:

1. **Countrywise Content Rating Classification**: Explore how content ratings are distributed across different countries.
2. **Distribution of Genres Across Countries**: Understand the prevalence of different genres in various countries' content offerings.
3. **Distribution of Genre and Rating**: Examine the relationship between genres and content ratings, revealing which genres are most associated with certain ratings.
4. **Correlation Analysis**: Determine the correlations within the dataset, highlighting any significant relationships between variables.
5. **Most Active Actors**: Identify the most active actors for movies and TV shows separately, showcasing the talents that dominate Netflix.
6. **Duration and Seasons Range**: Discover the typical duration range for movies and the number of seasons for TV shows, offering insights into content length.
7. **Average Content Duration**: Calculate the average duration for movies and TV show seasons, providing a general idea of content length.
8. **Content Addition Trends**: Find out when Netflix adds movies and TV shows most frequently over the years, months, and weekdays.
9. **Content Age Grouping**: Categorize content based on age group suitability, helping viewers choose content that matches their preferences.
10. **Top 10 Genres**: List the top 10 genres based on popularity within the Netflix library.
11. **Top 10 Directors**: Highlight the top 10 directors who have contributed significantly to Netflix's content.
12. **Content Distribution Across Countries**: Examine how content is distributed across different countries, showcasing Netflix's global reach.
13. **Distribution of Content**: Explore the distribution of content between movies and TV shows, revealing the balance in Netflix's offerings.

Explore this repository to uncover fascinating details about Netflix's content library!!!


