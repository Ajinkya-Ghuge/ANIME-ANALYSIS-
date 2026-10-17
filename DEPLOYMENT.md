# Deployment Guide for Render

## Prerequisites
- GitHub account with your code pushed to a repository
- Render account (free tier available at https://render.com)

## Deployment Steps

### Option 1: Using render.yaml (Recommended)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Add Render deployment configuration"
   git push origin main
   ```

2. **Connect to Render**
   - Go to https://dashboard.render.com
   - Click "New +" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` file
   - Click "Apply" to create the service

3. **Wait for deployment**
   - Render will install dependencies and start your app
   - Your app will be available at: `https://anime-analytics.onrender.com`

### Option 2: Manual Setup

1. **Create New Web Service**
   - Go to https://dashboard.render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure the service**
   - **Name**: anime-analytics
   - **Region**: Oregon (US West)
   - **Branch**: main
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`

3. **Environment Variables** (Click "Advanced" → "Add Environment Variable")
   - `PYTHON_VERSION` = `3.11.0`
   - `SECRET_KEY` = (generate a random string)
   - `FLASK_ENV` = `production`
   - `CORS_ORIGIN` = `*`

4. **Deploy**
   - Click "Create Web Service"
   - Wait 5-10 minutes for initial deployment

## Post-Deployment

### Access Your App
Your app will be available at: `https://[your-service-name].onrender.com`

### Monitor Logs
- Go to your service dashboard
- Click "Logs" tab to view real-time logs
- Check for any errors during startup

### Custom Domain (Optional)
1. Go to service "Settings"
2. Scroll to "Custom Domain"
3. Add your domain and follow DNS instructions

## Important Notes

### Free Tier Limitations
- **Spin down after inactivity**: Free services sleep after 15 minutes of inactivity
- **Cold starts**: First request after sleeping takes 30-50 seconds
- **Monthly hours**: 750 hours/month (enough for one service running 24/7)

### Performance Optimization
The app is configured with:
- 2 Gunicorn workers for handling concurrent requests
- 120-second timeout for long-running requests
- Production mode for Flask (debug=False)

### Troubleshooting

**Build fails**
- Check that `requirements.txt` is in the root directory
- Verify Python version compatibility
- Check build logs for specific error messages

**App won't start**
- Verify the start command in Render dashboard
- Check that `PORT` environment variable is used correctly
- Review application logs for startup errors

**500 errors**
- Check application logs in Render dashboard
- Verify all dependencies are installed
- Check for missing environment variables

**Static files not loading**
- Ensure `static` folder is committed to git
- Verify Flask static folder configuration in `app.py`
- Check browser console for 404 errors

### Updating Your App
Every push to your `main` branch triggers automatic redeployment:
```bash
git add .
git commit -m "Your update message"
git push origin main
```

## Support
- Render Documentation: https://render.com/docs
- Render Community: https://community.render.com

## Cost Estimate
- **Free Tier**: $0/month (with limitations)
- **Starter**: $7/month (no sleep, 512MB RAM)
- **Standard**: $25/month (1GB RAM, better performance)
