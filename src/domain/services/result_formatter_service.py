def format_result(intent, value):
    if value == 0:
        return "No data found for the selected period."

    if intent == "GMV":
        return f"Total GMV is ₹{value:,.2f}"
