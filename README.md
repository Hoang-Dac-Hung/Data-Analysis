# Describe

Dataset office_episodes.csv link https://www.kaggle.com/nehaprabhavalkar/the-office-dataset 
* `episode_number`: Canonical episode number.
* `season: Season` in which the episode appeared.
* `episode_title`: Title of the episode.
* `description`: Description of the episode.
* `ratings`: Average IMDB rating.
* `votes`: Number of votes.
* `viewership_mil`: Number of US viewers in millions.
* `duration`: Duration in number of minutes.
* `release_date`: Airdate.
* `guest_stars`: Guest stars in the episode (if any).
* `director`: Director of the episode.
* `writers`: Writers of the episode.
* `has_guests`: True/False column for whether the episode contained guest stars.
* `scaled_ratings`: The ratings scaled from 0 (worst-reviewed) to 1 (best-reviewed).

# Tasks

1. Create a matplotlib scatter plot of the data that contains the following attributes:

* Each episode's episode number plotted along the x-axis
* Each episode's viewership (in millions) plotted along the y-axis
* A color scheme reflecting the scaled ratings (not the regular ratings) of each episode, such that:
  >* Ratings < 0.25 are colored "red"
  >* Ratings >= 0.25 and < 0.50 are colored "orange"
  >* Ratings >= 0.50 and < 0.75 are colored "lightgreen"
  >* Ratings >= 0.75 are colored "darkgreen"
* A sizing system, such that episodes with guest appearances have a marker size of 250 and episodes without are sized 25
* A title, reading "Popularity, Quality, and Guest Appearances on the Office"
* An x-axis label reading "Episode Number"
* A y-axis label reading "Viewership (Millions)"
2. Provide the name of one of the guest stars (hint, there were multiple!) who was in the most watched Office episode. Save it as a string in the variable top_star (e.g. top_star = "Will Ferrell").
