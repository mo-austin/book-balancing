# Book-Balancing
This repository contains an algorithm to calculate how balanced a given ordering of books is based on their reading scores. The balance of a bookshelf is measured by comparing how often books have higher scores than the books to their left and right. A balanced shelf has similar numbers for these comparisons, and the balance score is the absolute difference between these counts.

##Problem Definition
Given a list of reading scores of books in the order they currently appear on the shelf, the goal is to calculate the balance score for the entire shelf.

##Installation and Use
1. Clone the repository:
   ```sh
   git clone https://github.com/mo-austin/book-balancing.git
   cd book-balancing
2. Run main script:
   ```sh
   python main.py

##Balance Calculation
1. Let L be the number of times any book has a higher score than the books to its left.
2. Let R be the number of times any book has a higher score than the books to its right.
3. The balance score B is defined as: B = ∣L − R∣

For example, given the shelf of books with reading scores:
S=[10,2,8,4,12]

L is 6 (12 is larger than everything to its left, 4 is larger than 2, and 8 is larger than 2).
R is 4 (10 is larger than three values to its right: 2, 8, and 4, and 8 is larger than 4).
The balance score B is:
B=∣6−4∣=2

##Solution (Divide and Conquer)
1. Divide: Split the array into two halves
2. Conquer: Recursively calculate L and R for each half
3. Combine: Merge the results from the two halves to compute the overall L and R

