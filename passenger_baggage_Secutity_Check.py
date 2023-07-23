#All passengers departing from the airport need to send their baggage for security check. Passengers may have more than one baggage. How will they make sure that all the baggage have undergone security check

number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
        if(security_check==True):
             print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
                 print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
