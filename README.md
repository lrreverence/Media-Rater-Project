# Media Rater Project

A web application that allows users to rate and review various types of media content. This platform enables users to share their opinions, discover new content, and connect with other media enthusiasts.

## Features

- User authentication (signup and login)
- Add and manage media links
- Rate and review media content
- View detailed media information
- User profile management
- Responsive design for all devices

## Tech Stack

### Backend
- **Django 5.1.4**: A high-level Python web framework
- **SQLite**: Lightweight database for development
- **Python**: Primary programming language

### Frontend
- **HTML5**: Structure of web pages
- **CSS**: Styling and layout
- **Django Templates**: Dynamic content rendering
- **Bootstrap**: Responsive design framework

### Development Tools
- **Git**: Version control
- **Vercel**: Deployment platform

## Project Structure

```
Media-Rater-Project/
├── core/              # Core application with base templates and shared functionality
├── link/              # Media link management app
├── user/              # User authentication and profile management
├── mediarater/        # Project configuration
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
└── vercel.json        # Vercel deployment configuration
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/lrreverence/Media-Rater-Project.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 