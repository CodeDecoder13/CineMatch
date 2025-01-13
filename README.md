# CineMatch: A Personalized Movie Recommendation System 🎬

## Overview
CineMatch is a data-driven movie filtering application designed to help users discover movies based on their preferences. By leveraging data wrangling techniques and filtering mechanisms, the system provides movie suggestions based on genre and release year to enhance your movie selection experience.

## Features 🌟
- **Genre-based Filtering**: Find movies in your preferred genre
- **Year-based Selection**: Filter movies by release year
- **Interactive UI**: User-friendly interface built with Streamlit
- **Real-time Results**: Instant movie filtering
- **Detailed Information**: View comprehensive movie details including:
  - Movie overview
  - Ratings and votes
  - Popularity metrics
  - Release dates
  - Genre classifications

## Technology Stack 💻
- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and filtering
- **Data Wrangling**: Efficient data processing and organization
- **Dataset**: Comprehensive movie database

## Installation Guide 🚀

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/codedecoder13/CineMatch-A-Personalized-Movie-Recommendation-System.git
   cd CineMatch-A-Personalized-Movie-Recommendation-System
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # For Windows
   python -m venv .venv
   .venv\Scripts\activate.ps1

   # For Linux/Mac
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   cd app
   streamlit run app.py
   ```

## Usage Guide 📖
1. Launch the application using the instructions above
2. Select your preferred movie genre from the dropdown menu
3. Choose a release year using the slider
4. Click the "Search Movies" button
5. Browse through the filtered movies with detailed information

## Project Structure 📁
```
CineMatch/
├── app/
│   └── app.py           # Main Streamlit application
|   └── modified_dataset.csv # dataset clean
├── .venv/               # Virtual environment
├── datawrangling/
│   └── model.ipynb
|    └── movie_dataset.csv # unclean dataset
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## How It Works 🛠️
1. **Data Processing**: The application processes a comprehensive movie dataset
2. **Filtering Mechanism**: Users can filter movies based on:
   - Genre preferences
   - Release year
3. **Results Display**: Filtered results are displayed in an intuitive card format showing:
   - Movie titles and release years
   - Plot overviews
   - Ratings and popularity metrics
   - Genre information

## Contributing 🤝
Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏
- Movie dataset providers
- Streamlit community
- All contributors and supporters

## Special Thanks 🌟
Special thanks to the TMDB Movies Dataset provider on Kaggle. This project utilizes the comprehensive movie database from:
[TMDB Movies Dataset 2023 (930k+ movies)](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies/code)

## Contact 📧
For any queries or suggestions, please open an issue in the GitHub repository.

---
