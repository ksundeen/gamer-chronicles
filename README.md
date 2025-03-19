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
This is a React Typescript with a Material UI Styling solution Single Page Application (SPA) with operations that allow users to 
- Login Panel (Simple authentication UI)
- Map as the Main Component (Using MapLibre)
- Expandable Sidebar (Using Material UI's Drawer)
- React Router for navigation
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

# Getting Started
Follow this setup to contribute and build it locally.

1. Clone the repo.
    ```bash
    git clone https://github.com/ksundeen/gamer-chronicles.git
    cd gamer-chronicles
    ```

2. Decide which project to work on: the frontend or backend.
    ```bash
    # Update the frontend
    cd gamer-chronicles-frontend

    # Update the backend
    cd gamer-chronicles-backend
    ```

    Or start from scratch:

    > ## FRONTEND: 
    >> 1. Create and install packages for the react map libre project.
    >>```bash
    >>npx create-react-app gamer-chronicles-frontend --template typescript
    >>cd gamer-chronicles-frontend
    >>```
    >>
    >> 2. Install maplibre and router packages.
    >>```bash
    >>npm install maplibre-gl react-router-dom --save
    >>```
    >>
    >> 3. Install and configure a css library for styling.
    >>```bash
    >>npm install @mui/material @mui/icons-material @emotion/react @emotion/styled --save
    >>```
    >>
    >> 4. Run the project
    >>```bash
    >>npm start
    >>```
    >>
    >> 5. Project structure:
    >>```bash
    >>/src
    >>/components
    >>    SidePanel.tsx
    >>    Login.tsx
    >>    MapPage.tsx
    >>App.tsx
    >>index.tsx
    >>index.css
    >>```


    > ## BACKEND: 
    >> 1. Create and activate the virtual environment for installing additional python packages.
    >>
    >>```bash
    >># Create virtual environment.
    >>python -m venv venv
    >>
    >># On Windows:
    >>venv\Scripts\activate
    >>
    >># On macOS/Linux:
    >>source venv/bin/activate
    >>
    >># Upgrade pip
    >>pip install --upgrade pip
    >>```
    >> 2. Install dependencies
    >>   
    >>```bash
    >>pip install -r requirements.txt
    >>```
    >>
    >> 3. Configure environmental variables in .env
    >>```bash
    >>DATABASE_URL=postgresql://your_user:your_password@your_host/your_database
    >>JWT_SECRET=your_secret_key
    >>JWT_ALGORITHM=HS256
    >>ACCESS_TOKEN_EXPIRE_MINUTES=30
    >>```
    >>
    >> 4. Run database migrations if needed.
    >>```bash
    >>python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
    >>```
    >>
    >> 5. Run the FastAPI app. The API will be avaible.
    >>```bash
    >>uvicorn main:app --reload
    >>```
    >>
    >> 6. View API documentation. Once the app is running, open FastAPI:
    >>* Swagger UI → http://127.0.0.1:8000/docs
    >>* Redoc UI → http://127.0.0.1:8000/redoc