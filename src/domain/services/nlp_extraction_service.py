# It will work for single data 
# say...What is the total GMV for November

#   def extract_month(text):
#     months = {
#         "january": 1, "february": 2, "march": 3,
#         "april": 4, "may": 5, "june": 6,
#         "july": 7, "august": 8, "september": 9,
#         "october": 10, "november": 11, "december": 12
#     }

#     for name, number in months.items():
#         if name in text.lower():
#             return number

#     return None

#What is the total sum of GMV November and October?

def extract_months(text):
    months = {
        "january": 1, "february": 2, "march": 3,
        "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9,
        "october": 10, "november": 11, "december": 12
    }

    found = []
    text = text.lower()

    for name, number in months.items():
        if name in text:
            found.append(number)

    return found
