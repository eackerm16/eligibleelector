def check_voter_eligibility():
    """
    A friendly program to check if someone is eligible to vote.
    Includes encouraging messages and calculates years until eligibility.
    """
    print("👋 Welcome to the Voter Eligibility Checker! 👋")
    print("Let's find out if you can make your voice heard! 🗳️")
    
    try:
        # Get user's age and convert to integer
        age = int(input("\nHow old are you? "))
        
        # Check eligibility
        if age >= 18:
            print("\n🎉 Congratulations! You are eligible to vote. Go make a difference! 🎉")
        else:
            years_to_wait = 18 - age
            print(f"\n🌟 Oops! You're not eligible yet. But hey, only {years_to_wait} more years to go! 🌟")
            print("Keep learning and growing - your future vote will matter! 💪")
            
    except ValueError:
        print("\n❌ Oops! Please enter a valid number for your age.")
    except Exception as e:
        print(f"\n❌ Something went wrong: {str(e)}")

if __name__ == "__main__":
    check_voter_eligibility() 