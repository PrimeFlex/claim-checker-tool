from checker import assess_claim_viability

def get_input():
    try:
        estimate = float(input("Enter estimated damage ($): "))
        deductible = float(input("Enter your deductible ($): "))
        damage_type = input("Type of damage (roof, hail, water, fire, etc): ")
        days = int(input("Days since damage occurred: "))
        return estimate, deductible, damage_type, days
    except:
        print("Invalid input. Please try again.")
        return get_input()

if __name__ == "__main__":
    estimate, deductible, damage_type, days = get_input()
    result = assess_claim_viability(estimate, deductible, damage_type, days)
    print("\n--- Recommendation ---")
    print(result)
