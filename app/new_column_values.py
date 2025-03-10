from datetime import datetime

new_column_value = {
    "new_column_value": [
        {
            "String": "",
            "Integer": 0,
            "Float": 0.0,
            "Boolean": False,
            "Date": datetime.today().strftime('%Y-%m-%d'),
            "Time": datetime.now().strftime('%H:%M:%S')
        }
    ]
}