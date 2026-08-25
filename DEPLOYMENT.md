# Deployment Guide

This project is split into two deployable parts:

- Frontend: Astro on Vercel
- Backend: FastAPI on Render

The backend calls the Brawl Stars API through Fixie so the outbound IP stays stable.

## 1. Fixie

1. Create a Fixie account.
2. Create an HTTP proxy.
3. Copy the `FIXIE_URL` value Fixie gives you.
4. Copy the two static outbound IP addresses shown by Fixie.
5. Add those two IPs to the Brawl Stars developer portal allowlist.

Keep `FIXIE_URL` private. You will use it only in Render.

## 2. Render backend

### What to create

Create a new **Web Service** on Render.

### What to connect

Connect the GitHub repository that contains this project.

### Settings

- Root directory: `backend`
- Runtime: `Python`
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Environment variables

Add these variables in the Render dashboard:

- `BRAWL_STARS_TOKEN` or `BRAWL_API_KEY`
- `FIXIE_URL`
- `CORS_ORIGINS`
- `CORS_ORIGIN_REGEX`

Suggested values:

- `CORS_ORIGINS=http://localhost:4321,http://127.0.0.1:4321,https://your-frontend.vercel.app`
- `CORS_ORIGIN_REGEX=https://.*\.vercel\.app`

### Deploy

1. Save the service.
2. Wait for the first deploy to finish.
3. Copy the Render service URL, for example `https://your-api.onrender.com`.

## 3. Vercel frontend

### What to create

Import the same GitHub repository into Vercel as a new project.

### Settings

- Root directory: `frontend`
- Framework preset: Astro

### Environment variables

Add this variable in Vercel:

- `PUBLIC_API_URL=https://your-api.onrender.com`

If you are testing locally, you can use:

- `PUBLIC_API_URL=http://127.0.0.1:8000`

### Deploy

1. Save the project.
2. Deploy it.
3. Copy the Vercel URL, for example `https://your-app.vercel.app`.

## 4. Final Render update

After Vercel gives you the final frontend URL:

1. Go back to Render.
2. Update `CORS_ORIGINS` to include the exact Vercel URL.
3. Redeploy the backend.

This is the final step that allows the browser to call Render from the Vercel-hosted frontend.

## 5. Local development

Use these values locally:

### Backend

- `BRAWL_STARS_TOKEN=...`
- `FIXIE_URL=...` if you want local requests to go through Fixie too

### Frontend

- `PUBLIC_API_URL=http://127.0.0.1:8000`

## 6. Files added for deployment

- [`backend/requirements.txt`](backend/requirements.txt)
- [`backend/.env.example`](backend/.env.example)
- [`frontend/.env.example`](frontend/.env.example)
- [`render.yaml`](render.yaml)

## 7. Notes

- The backend reads `PUBLIC_API_URL` only in the frontend.
- The backend uses `FIXIE_URL` for outbound calls to the Brawl Stars API.
- The frontend must point to the Render backend URL, not `localhost`, once deployed.
