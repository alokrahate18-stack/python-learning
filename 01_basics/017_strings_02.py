message = "I am learning Python!"
message_length = len(message)

print(message)
print(len(message))
print(message_length)

print(message[0:7]) # Here, the first number i.e. 0 indicates starting from index 0 and the second number indicates nos. of characters.
print(message[0:-6]) # Here, -6 indicates as len(message)-6 characters in the backend.
print(message[-6:-4]) # Here, the first digit i.e. -6 indicate 6th letter from backward. Backward index does not include 0.
print(message[-6-4]) # Here, -6-4 = -10. So, it directly prints the 10th letter from backward.
