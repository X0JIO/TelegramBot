from flask import Flask, jsonify
from google.oauth2.service_account import Credentials
import gspread

app = Flask(__name__)

# Настройка Google Sheets API
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
creds = Credentials.from_service_account_file('C:\\Users\\XOJIO\\Desktop\\TelegramBot\\telegrambot-458211-bf60fba2fd79.json', scopes=scope)
client = gspread.authorize(creds)

@app.route('/get-data', methods=['GET'])
def get_data():
    try:
        spreadsheet = client.open("11M")  # Замените на название вашей таблицы
        worksheet = spreadsheet.sheet1  # Или укажите конкретный лист
        data = worksheet.get_all_records()  # Получаем все данные в виде списка словарей

        return jsonify(data)  # Возвращаем данные в формате JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
