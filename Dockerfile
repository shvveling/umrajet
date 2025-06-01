FROM python:3.10-slim

# Ishchi papkani o‘rnatish
WORKDIR /app

# Fayllarni konteynerga nusxalash
COPY . .

# Kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Botni ishga tushirish
CMD ["python", "bot.py"]
