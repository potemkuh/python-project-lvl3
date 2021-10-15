FROM python

WORKDIR /app

COPY . .

CMD ['python', 'page_loader/scripts/page_loader.py']
