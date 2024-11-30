import random

# Constants
TOTAL_CARGO_WEIGHT = 713  # Total weight of all boxes
NUM_BOXES = 3  # Number of boxes
MAX_DISTANCE = 7  # Distance in kilometers

# Initialize boxes with random locations and weights
def initialize_boxes():
    weights = [random.randint(100, 300) for _ in range(NUM_BOXES - 1)]
    weights.append(TOTAL_CARGO_WEIGHT - sum(weights))  # Ensure total weight is 713 kg
    locations = [random.randint(1, MAX_DISTANCE) for _ in range(NUM_BOXES)]
    return locations, weights

# Check if entered marks match current locations
def check_marks(locations, marks):
    return set(locations) == set(marks)

# Move boxes to new random locations
def move_boxes():
    return [random.randint(1, MAX_DISTANCE) for _ in range(NUM_BOXES)]

def main():
    print("Welcome, Martians! Let's find your buried cargo.")
    print("Enter 3 kilometer marks to locate the boxes.")
    print("Be careful: if the marks are wrong, the boxes will move!")
    
    locations, weights = initialize_boxes()

    while True:
        try:
            # Input marks from the user
            marks = []
            for i in range(NUM_BOXES):
                mark = int(input(f"Enter the kilometer mark for box {i + 1} (1-{MAX_DISTANCE}): "))
                if not 1 <= mark <= MAX_DISTANCE:
                    raise ValueError("Invalid distance! Must be between 1 and 7.")
                marks.append(mark)
            
            # Check if marks match the box locations
            if check_marks(locations, marks):
                total_weight = sum(weights)
                if total_weight == TOTAL_CARGO_WEIGHT:
                    print(f"Congratulations! You've found all the boxes with a total weight of {TOTAL_CARGO_WEIGHT} kg.")
                    break
                else:
                    print("The weights do not add up correctly. Try again!")
            else:
                print("Incorrect locations! The boxes have moved.")
                locations = move_boxes()
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
