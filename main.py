# Pass or Fail Finder Based on Marks

PASS_MARKS = 40

def main():
    try:
        marks = float(input("Enter your marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Please enter a value between 0 and 100.")
        elif marks >= PASS_MARKS:
            print(f"Result: PASS (You scored {marks:g}/100)")
        else:
            print(f"Result: FAIL (You scored {marks:g}/100)")

    except ValueError:
        print("Invalid input! Please enter marks as a number.")

if __name__ == "__main__":
    main()
