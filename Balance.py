

class Balance:

    def __init__(self):
        return

    # This method is the main entry point for calculating the balance
    def compute(self, shelf):
        balance_values = self.calculate_balance(shelf, 0, 0)
        # We return the absolute difference between the left and right weights
        return abs(balance_values[1] - balance_values[2])

    # This method recursively calculates the balance of the shelf
    def calculate_balance(self, shelf, left_weight, right_weight):
        # Base case: if the shelf has only one book, we return immediately
        if len(shelf) == 1:
            return shelf, 0, 0  

        #  divide the shelf into two halves
        mid_point = len(shelf) // 2
        #  recursively calculate the balance for the left half
        left_half, left_weight, right_weight = self.calculate_balance(shelf[:mid_point], 0, 0)
        #  recursively calculate the balance for the right half
        right_half, additional_left_weight, additional_right_weight = self.calculate_balance(shelf[mid_point:], 0, 0)

        #  merge the two halves back together
        merged_shelf = []
        total_left_weight = left_weight + additional_left_weight
        total_right_weight = right_weight + additional_right_weight
        left_index, right_index = 0, 0

        #  iterate over the books in the two halves
        while left_index < len(left_half) and right_index < len(right_half):
            # If the book in the left half is lighter,  add it to the merged shelf
            # and update the total left weight
            if left_half[left_index] < right_half[right_index]:
                merged_shelf.append(left_half[left_index])
                left_index += 1
                total_left_weight += len(right_half) - right_index
            # If the book in the right half is lighter,  add it to the merged shelf
            # and update the total right weight
            elif left_half[left_index] > right_half[right_index]:
                merged_shelf.append(right_half[right_index])
                right_index += 1
                total_right_weight += len(left_half) - left_index
            # If the books are of the same weight,  add all duplicates to the merged shelf
            # and update the total weights accordingly
            else:
                left_duplicates = 0
                right_duplicates = 0
                current_book = left_half[left_index]
                while left_index < len(left_half) and left_half[left_index] == current_book:
                    merged_shelf.append(left_half[left_index])
                    left_index += 1
                    left_duplicates += 1
                    total_left_weight += (len(right_half) - right_index)

                while right_index < len(right_half) and right_half[right_index] == current_book:
                    merged_shelf.append(right_half[right_index])
                    right_index += 1
                    right_duplicates += 1
                    total_right_weight += len(left_half) - left_index

                total_left_weight -= right_duplicates * left_duplicates

        #  add any remaining books from the left half to the merged shelf
        while left_index < len(left_half):
            merged_shelf.append(left_half[left_index])
            left_index += 1

        #  add any remaining books from the right half to the merged shelf
        while right_index < len(right_half):
            merged_shelf.append(right_half[right_index])
            right_index += 1

        #  return the merged shelf and the total weights
        return merged_shelf, total_left_weight, total_right_weight