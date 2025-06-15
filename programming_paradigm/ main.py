import sys
from robust_division_calculator import safe_divide

def main():
    
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1) # Exit with an error code

    numerator_arg = sys.argv[1]
    denominator_arg = sys.argv[2]

    result_message = safe_divide(numerator_arg, denominator_arg)
    
    print(result_message)

if __name__ == "__main__":
    main()