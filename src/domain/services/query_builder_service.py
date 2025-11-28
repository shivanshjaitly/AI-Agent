        # It will work for single data 
        # say...What is the total GMV for November


# def build_query(intent, month):
#     if intent == "GMV":
#         return f"""
#         SELECT SUM(order_value) AS total_gmv
#         FROM XYZ
#         WHERE MONTH(order_date) = {month}
#         """

def build_query(metric, months):

    # if intent == "GMV" and months:
    #     month_list = ",".join(map(str, months))
    #     return f"""
    #     SELECT SUM(order_value)
    #     FROM XYZ
    #     WHERE MONTH(order_date) IN ({month_list})
    #     """

    # return None

    if metric.lower() == "gmv":
        months_sql = ",".join(map(str, months))
        return f"""
        SELECT SUM(order_value)
        FROM XYZ
        WHERE MONTH(order_date) IN ({months_sql})
        """

    return None

