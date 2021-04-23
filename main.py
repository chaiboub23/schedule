from icalendar import Calendar, Event
from datetime import datetime as dt
import json
import re
g = open('test.ics', 'rb')
gcal = Calendar.from_ical(g.read())
new_cal = []
temp = []
regexp = re.compile(r'C([1-8])')
for component in gcal.walk():
    if component.name == "VEVENT":
        summary = component.get('summary')
        # time = str(component.get('dtstart').dt)
        if "Day" in summary or regexp.search(summary):
            if temp == []:
                continue
            else:
                new_cal.append(temp)
                temp = []
            continue
        temp.append(summary)
        # new_cal_arr_two.append(val)
g.close()
with open('test.json', 'w') as test_file:
    test_file.write(json.dumps(new_cal, indent=4))

