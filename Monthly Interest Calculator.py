# Monthly Interest Calculation
# This script calculates the monthly interest based on a given principal and APR (Annual Percentage Rate).
# It also allows the user to input multiple principal amounts and APRs, calculates their monthly interest, and averages them.


def calc_monthly_interest(principal, apr_percent, decimals=2):
    if principal <= 0 or apr_percent <= 0:
        raise ValueError("Principal and APR must be positive numbers.")
    monthly_rate = apr_percent / 100 / 12
    return round(principal * monthly_rate, decimals)


# Example with user input
try:
    print("""Beginning the Monthly Interest Calculation""")
    principal_a = float(input("Enter the principal amount for 'a': "))
    # print(principal_a)
    apr_percent_a = float(input("Enter the APR percentage: "))
    # print(apr_percent_a)
    a = calc_monthly_interest(principal_a, apr_percent_a)
    print(f"""The monthly intrest is: {a}""")

    principal_b = float(input("\nNow lets do another Monthly Intrest Calculation. Enter the principal amount for 'b': "))
    # print(principal_b)
    apr_percent_b = float(input("Enter the APR percentage: "))
    # print(apr_percent_b)
    b = calc_monthly_interest(principal_b, apr_percent_b)
    print(f"""The monthly intrest is: {b}""")

    principal_c = float(input("\nNow lets do another Monthly Intrest Calculation. Enter the principal amount for 'c': "))
    # print(principal_c)
    apr_percent_c = float(input("Enter the APR percentage: "))
    # print(apr_percent_c)
    c = calc_monthly_interest(principal_c, apr_percent_c)
    print(f"""The monthly intrest is: {c}""")

    if c == 0:
        print("Error: Division by zero is not allowed.")
    else:
        principal_average = (principal_a + principal_b + principal_c) / 3
        apr_average = (apr_percent_a + apr_percent_b + apr_percent_c) / 3
        d = calc_monthly_interest(principal_average, apr_average)
        print(f"""\nThe average principal is: {principal_average}""")
        print(f"""The average APR is: {apr_average}""")
        print(f"""The resulting monthly dividend with your principal_average by apr_average is: {d}""")
        # print(f"The result of dividing a by c is: {a / c}")
        # print(f"The result of dividing b by c is: {b / c}")
        # print(f"The result of dividing a by b is: {a / b}")


except ValueError as e:
    print(f"Input error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Thank you for using the Monthly Interest Calculator.")
    print("Goodbye!")
