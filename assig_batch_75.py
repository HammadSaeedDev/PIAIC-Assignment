# Quesstion # 01
print("==============================")
print("QUESTION NO 1")
print("\n")
Principle = 5000
Rate = 8
Time = 1

Amount = Principle * (1 + Rate/100)**Time

print("Principl Amount: $", Principle)
print("Rate of interet: ", Rate,"%")
print("Time Period: ", Time,"Year")
print("Final Amount: $", round(Amount, 2))
print("")

# Quesstion # 02
print("==============================")
print("QUESTION NO 2")
print("\n")

radius = 7
height = 10
tsa = 2*3.1416*radius**2 + 2*3.1416*radius*height 
print("total surface area of a cylinder: ",tsa)

# Quesstion # 03
print("==============================")
print("QUESTION NO 3")
print("\n")

hours = 2
minutes = 46
seconds = 40
total_seconds = (hours * 3600) + (minutes * 60) + seconds
print("Total seconds" , total_seconds)

# Quesstion # 04``
print("==============================")
print("QUESTION NO 4")
print("\n")
total_bill = 2750
tip_percent = 10 # in percent
number_of_people = 5 

tip_amount = (tip_percent / 100) * total_bill
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / number_of_people

print("Each person pays: ₹", amount_per_person)

# Quesstion # 05
print("==============================")
print("QUESTION NO 5")
print("\n")

subjects = {
    "Math": (80, 3),
    "Physics": (75, 4),
    "Chemistry": (70, 3)
}

weighted_sum = 0
total_weight = 0

for subject, (score, weight) in subjects.items():
    weighted_sum += score * weight
    total_weight += weight

weighted_average = weighted_sum / total_weight

print("Weighted Average Marks:", weighted_average)

# Quesstion # 06
print("==============================")
print("QUESTION NO 6")
print("\n")

speed_kmph = 72
distance_m = 500

speed_mps = speed_kmph * (5 /18)

time_seconds = distance_m / speed_mps

print("Speed in m/s:", speed_mps)
print("Time to cover 500 meters:", time_seconds, "seconds")

# Quesstion # 07
print("==============================")
print("QUESTION NO 7")
print("\n")

original_price = 1000
first_discount = 10  # in percent
second_discount = 5

price_after_first = original_price * (1 - first_discount / 100)

final_price = price_after_first * (1 - second_discount / 100)

amount_saved = original_price - final_price
effective_discount_percent = (amount_saved / original_price) * 100

print("Final price after both discounts:", final_price)
print("Total amount saved:", amount_saved)
print("Effective discount %:", effective_discount_percent)

# Quesstion # 08
print("==============================")
print("QUESTION NO 8")
print("\n")

numbers = [100, 200, 300, 400, 500]

increased_numbers = [num * 1.10 for num in numbers]

average = sum(increased_numbers) / len(increased_numbers)

print("Increased numbers:", increased_numbers)
print("Average after 10% increase:", round(average, 2))

# Quesstion # 09
print("==============================")
print("QUESTION NO 9")
print("\n")

total_seconds = 10000

hours = total_seconds // 3600

remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60

seconds = remaining_seconds % 60

print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")


# Quesstion # 10
print("==============================")
print("QUESTION NO 10")
print("\n")

P = 100000 
annual_rate = 12
R = annual_rate / (12 * 100)
N = 12 

EMI = P * R * (1 + R) ** N / ((1 + R) ** N - 1)

print(f"Monthly EMI: ₹{EMI:.2f}")