'''
DEVELOPER(S): Marquez Ramirez
COLLABORATOR(S): None
'''
"""
This program will be used to help students estimate how much money they need to graduate.

In this program there will be many inputs for the user such as (savings, remaining credits needed, tuition cost, additional expenses, and financial aid). The purpose of this program is to take these inputs from the user and calculate the total amount of money needed to graduate. This program will also be able to know if the student has enough money to graduate or how much they need to save. The final output of the program will result in a positive number (How much money the student will have left after tuition cost) or it will result in a negative number (How much the student needs to save to pay for tuition). Fianlly the program will also take the data the user has submitted as well as the final cost difference and will place this data formatted into a file that the student can use later.
"""

##########################################
import os
# 
##########################################
# No imports are going to be needed.


##########################################
# FUNCTIONS:
##########################################
def calc_tuition_cost(credits, cost_per_credits):
    """ This function will return the cost of total tuition based on remaining credits needed"""
    return credits * cost_per_credits
    

def calc_total_after_aid(tuition_cost, aid):
    """This function will return the total after financial aid is taken into account"""
    return tuition_cost - aid

def calc_cost_difference(saved, total_cost):
    """This function will return the total needed or left over based on the amount user has saved minus the total cost"""
    return saved - total_cost

def save_tuition_report(data):
    '''This will save the calculations into a text file'''

    with open("tuition_report.txt", "w") as file:
        file.write("---College Tuition Report ---\n")
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
        file.write("--------------------------")
    print("\n Report has been successfully saved to tuition_report.txt")

    



##########################################
# MAIN PROGRAM:
##########################################
def main():
    print("============================")
    print("College Tuition Calculator")
    print("============================")

    try:
        #Getting the student information
        student_name = input("What is your name?\n").title()
        money_saved = float(input("How much money do you have saved?\n"))
        credits_remaining = int(input("How many credits do you need to graduate?\n"))
        cost_per_credit = float(input("How much does each credit cost?\n"))
        aid_amount = float(input("How much aid will you recieve?\n"))

        #Calculating costs of tuition
        tuition_cost = calc_tuition_cost(credits_remaining, cost_per_credit)
        total_cost = calc_total_after_aid(tuition_cost, aid_amount)
        cost_difference = calc_cost_difference(money_saved, total_cost)

        #storing the data insdie of a dictionary
        data_summary = {
            "Student Name": student_name,
            "Credits Remaining": credits_remaining,
            "Cost Per Credit": f"${cost_per_credit:.2f}",
            "Tuition Subtotal": f"${tuition_cost:.2f}",
            "Aid Applied": f"${aid_amount:.2f}",
            "Total Out-of-Pocket": f"${total_cost:.2f}",
            "Remaining Savings": f"${cost_difference:.2f}"
        }

        #Final Output

        print("\n------- Financial Summary -------")
        print(f"Student: {student_name}")
        print(f"Credits Remaining: {credits_remaining}")
        print(f"Estimated Tuition: ${tuition_cost:.2f}")
        print(f"Final Balance: ${total_cost:.2f}")

        if cost_difference >= 0:
            print(f"Final Status: You have enough saved for tuition! (${cost_difference:.2f} left over)")
        else:
            print(f"Financial Status: You don't have enough money you are short by ${abs(cost_difference):.2f}")

        #Savings the dictionary data to the file
        save_tuition_report(data_summary)
    
    except ValueError:
        print("\n[Error] Please enter valid numbers for financial values.")



if __name__ == "__main__":
    main()