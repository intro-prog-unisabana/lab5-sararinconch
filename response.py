def input_response(numero_aleatorio, user_input):
    if user_input < numero_aleatorio:
        return ("Too low! Try a higher number.", False)
    elif user_input > numero_aleatorio:
        return ("Too high! Try a lower number.", False)
    else:
        return("Correct! You guessed the number!", True)