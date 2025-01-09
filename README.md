# Movies Metadata Analysis

This repository provides an analysis of movie metadata using Python. It explores techniques to filter, analyze, and visualize data using a large dataset of movies.

## Project Structure

- `movies.py`: Python script for data processing and analysis.
- `movies_metadata.csv`: Dataset containing metadata for movies.
- `5.4. Filtering the Data — How to Think Like a Data Scientist.pdf`: Documentation on filtering and analyzing movie data.

## Dataset Description

The dataset (`movies_metadata.csv`) contains metadata about movies, including:

- **Title**: Name of the movie.
- **Budget**: Production budget of the movie.
- **Revenue**: Box office revenue.
- **Genres**: Categories of the movie (e.g., Action, Comedy).
- **Release Date**: Date the movie was released.
- **Runtime**: Duration of the movie in minutes.
- **Popularity**: Popularity score based on various factors.

## Objectives

1. Filter and explore movies with specific criteria (e.g., budget over $1M).
2. Analyze movie data by genres, budgets, and other factors.
3. Visualize patterns and trends in the movie industry.

## Requirements

- Python 3.8+
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/movies-analysis.git
   cd movies-analysis
   ```

2. Run the analysis script:

   ```bash
   python movies.py
   ```

3. The script performs tasks such as:
   - Filtering movies by budget and other criteria.
   - Summarizing data using descriptive statistics.
   - Creating visualizations (e.g., bar plots, histograms).

## Key Findings

- **Filtering**: Identified 7,208 movies with a budget over $1M.
- **Analysis**: Explored relationships between budgets and revenues, genre popularity, and more.
- **Visualization**: Displayed data trends with charts and graphs for deeper insights.

## Future Work

- Extend analysis to include data on directors, actors, and production companies.
- Build predictive models for movie success based on budget and other factors.
- Develop an interactive dashboard for users to explore movie data.

## References

- "How to Think Like a Data Scientist" - Filtering the Data

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Contributions, suggestions, and feedback are welcome! Feel free to submit issues or pull requests.
