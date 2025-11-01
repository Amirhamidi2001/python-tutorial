import requests
import os
import mysql.connector
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

mydb = mysql.connector.connect(
    host=DB_HOST, user=DB_USER, password=DB_PASS, database="countries"
)
mycursor = mydb.cursor()

# Ensure table exists
mycursor.execute(
    """
CREATE TABLE IF NOT EXISTS countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    population BIGINT,
    area FLOAT
)
"""
)

url = "https://www.scrapethissite.com/pages/simple/"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
except requests.RequestException as e:
    print(f"Request failed: {e}")
    exit(1)

soup = BeautifulSoup(r.text, "html.parser")
countries = soup.find_all(class_="col-md-4 country")

for country in countries:
    name = country.find(class_="country-name").get_text(strip=True)
    population = country.find(class_="country-population").get_text(strip=True)
    area = country.find(class_="country-area").get_text(strip=True)

    population = int(population.replace(",", "")) if population else None
    area = float(area.replace(",", "")) if area else None

    sql = """
    INSERT INTO countries (name, population, area)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE
    population = VALUES(population),
    area = VALUES(area)
    """

    try:
        mycursor.execute(sql, (name, population, area))
    except mysql.connector.Error as err:
        print(f"MySQL Error for {name}: {err}")

mydb.commit()
print("Data inserted successfully!")
