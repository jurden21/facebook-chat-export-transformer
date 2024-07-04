import json
import datetime

json_name = "result.json"
json_file = open(json_name, "r", encoding="UTF-8")
json_data = json.load(json_file)

text_name = "text.txt"
text_file = open(text_name, "w", encoding="UTF-8")

for message in json_data["messages"]:
    datetime_value = datetime.datetime.fromtimestamp(message["timestamp_ms"] / 1e3)
    date_value = str(datetime_value.date())
    time_value = str(datetime_value.time())[0:8]
    sender_value = message["sender_name"].encode('raw_unicode_escape').decode('utf-8')
    message_text = message["content"].encode('raw_unicode_escape').decode('utf-8')

    text_file.write(date_value + " " + time_value + " - " + sender_value + ": " + message_text + "\n")
    print(date_value + " " + time_value + " - " + sender_value + ": " + message_text)
