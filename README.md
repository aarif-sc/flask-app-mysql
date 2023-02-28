Python 3.8.10 
python3 -m venv venv_sql 
source venv_sql/bin/activate
==================================
Write basic flask app with two apis

get api /settime - send time (HH:MM) in url params and return cookie the same value
post api /isitemavailable - send csv and run the params through the isitemavailable logic then return response csv request item_name - timestring dosa - 17:00-21:00,7:00-10:00,10:45-12:0 vada - 18:45-22:00,6:30-11:00,09:55-13:0
cookie is sent automatically

response csv message dosa available vada not available

Note: can use google given input & output are just sample comparison should happen between datetime objs