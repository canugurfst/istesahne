# Deployment Checklist

## Normal Deployment

1. git add .
2. git commit -m "Description"
3. git push
4. Wait for Railway deployment
5. Check homepage
6. Check admin

## If Models Changed

railway ssh
python manage.py migrate

## If Static Files Break

railway ssh
python manage.py collectstatic --noinput