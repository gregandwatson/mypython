#!/usr/bin/python

cover_price = 24.95
discount = .40
shipping = 3.00
additional = .75
no_of_copies = 60

discount_price = cover_price - (cover_price * discount)
final_book_price = discount_price * no_of_copies
total_shipping = 3.00 + (no_of_copies * additional)
total_price = final_book_price + total_shipping

print(total_price) 
