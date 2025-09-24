# SGGSIET CMS Starter

This is a starter repository for SGGSIET Nanded academic CMS using Flask + PostgreSQL.
It is preconfigured for development with Docker Compose and ready to deploy to DigitalOcean App Platform.

## Quick start (with Docker)

1. Copy `.env.example` to `.env` and edit as needed.
2. Build and run:
   ```
   docker compose up --build
   ```
3. Run migrations inside the container:
   ```
   docker compose exec web flask db init
   docker compose exec web flask db migrate -m "init"
   docker compose exec web flask db upgrade
   ```
4. Create admin user:
   ```
   docker compose exec web flask shell
   # then in shell:
   from app import db
   from app.models import User
   u = User(email='admin@sggsiet.ac.in', name='Admin', role='admin')
   u.set_password('YourStrongPassword')
   db.session.add(u)
   db.session.commit()
   ```

## Deploy to DigitalOcean App Platform

- Push this repo to GitHub.
- Create a DigitalOcean App and connect to GitHub.
- Use Dockerfile build.
- Set environment variables (DATABASE_URL -> managed postgres, SECRET_KEY, MEDIA_PROVIDER=spaces, DO_SPACE_* keys).
- Add a release command: `flask db upgrade`
- Deploy.

## Notes

- Replace `is_accessible` in admin views with proper admin checks.
- For production, use DigitalOcean Managed PostgreSQL and DigitalOcean Spaces for media.
