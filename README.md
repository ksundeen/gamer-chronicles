# Gamer Chronicles

## Purpose of Gamer Chronicles
This application shows the geovisualizations of any favorite video, card, or board games that users are willing to share any details about and statistics associated with them. The application will prompt the user to enter these attributes about a game: title, creator, manufacturer, original release date, summary or game, game genre (playing characteristics), and game type (video, card, or board game). The one requirement is that the location entered is the original location where the game idea was developed, not where the game was produced or manufactured. The goal is to identify hubs of gamer creativity where games were created. 

## Goals of Gamer Chronicles
1. To connect users interested in digital (video, streaming) and analog (board, cards) gaming globally to share favorite and memorable game titles. 
2. To allow users to share interesting stories, pictures, videos, and information about games.
3. To inspire new or modified game ideas.
4. To see where in the world different game ideas were originally generated or created.
5. Identify hubs of creativity in the gaming world.

# Tech Stack
## Frontend
This is a React Typescript Single Page Application (SPA) with operations that allow users to 
- Login
- Create a profile
- Add a location of a game
- Enter details about the game, including title, description, and upload a picture
- Select an icon to represent the type of game genre
- Geovisualizations will include 
  - displaying the types of game genre
  - sliders of years of game creation 
  - numbers of interested game players
  - typical game play time
  - level of complexity

## Backend
This is a FastAPI application with CRUD operations, JWT authentication, and a PostgreSQL database connection. The project is designed with best practices for security, scalability, and ease of use.

### Features
- User Authentication (JWT-based login & register)
- CRUD operations with PostgreSQL
- Secure password hashing with bcrypt
- Dependency-managed virtual environment
- FastAPI interactive API docs (/docs)
- Easy deployment-ready setup