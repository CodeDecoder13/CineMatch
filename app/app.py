import streamlit as st
import pandas as pd
import time

# Load the dataset
@st.cache_data
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"Error: Could not find the file {file_path}")
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# Filter dataset based on user input
def recommend_apps(data, genre, release_year):
    filtered_data = data[
        (data['genres'].str.contains(genre, case=False, na=False)) &
        (pd.to_datetime(data['release_date'], errors='coerce').dt.year == release_year)
    ]
    return filtered_data.sort_values('vote_average', ascending=False)

# Streamlit app
def main():
    st.set_page_config(
        page_title="Movie Recommendation System",
        page_icon="🎬",
        layout="wide"
    )
    
    st.title("🎬 CineMatch")
    st.write("Discover movies based on your preferences!")
    
    # Load dataset with a spinner
    with st.spinner('Loading movie database...'):
        file_path = 'modified_dataset.csv'
        data = load_data(file_path)
    
    if data is None:
        st.stop()
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.header("🎯 Filter Options")
        
        # Genre selection with search
        genres = sorted(data['genres'].dropna().unique())
        selected_genre = st.selectbox(
            "Select Genre",
            genres,
            help="Choose your preferred movie genre"
        )
        
        # Release year selection with slider
        data['release_year'] = pd.to_datetime(data['release_date'], errors='coerce').dt.year
        min_year = int(data['release_year'].min())
        max_year = int(data['release_year'].max())
        selected_year = st.slider(
            "Select Release Year",
            min_value=min_year,
            max_value=max_year,
            value=2020,
            help="Choose the movie release year"
        )
        
        # Add a search button
        search = st.button("🔍 Search Movies", use_container_width=True)
    
    with col2:
        if search:
            with st.spinner('Finding movies for you...'):
                recommendations = recommend_apps(data, selected_genre, selected_year)
            
            if not recommendations.empty:
                st.header(f"🎉 Found {len(recommendations)} Movies")
                
                # Display each movie in a card-like format
                for _, movie in recommendations.iterrows():
                    with st.container():
                        st.markdown("---")
                        st.subheader(f"{movie['title']} ({pd.to_datetime(movie['release_date']).year})")
                        cols = st.columns([2, 1])
                        with cols[0]:
                            st.write("📝 **Overview:**")
                            st.write(movie['overview'])
                        with cols[1]:
                            st.write(f"⭐ **Rating:** {movie['vote_average']:.1f}/10")
                            st.write(f"🗳️ **Votes:** {movie['vote_count']:,}")
                            st.write(f"📈 **Popularity:** {movie['popularity']:.1f}")
                            st.write(f"🎭 **Genres:** {movie['genres']}")
            else:
                st.info("No movies found matching your criteria. Try adjusting the filters!")

if __name__ == "__main__":
    main()
