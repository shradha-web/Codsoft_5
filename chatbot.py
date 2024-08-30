def chatbot_response(user_input):



  if "Hello" in user_input or "Hii" in user_input or "Hey" in user_input:
    return "Hello! How can I help you ?"
  elif "what are you doing now?"in user_input:
    return "Currently i am assisting you."
  elif "How are you?" in user_input:
    return "I am fine, What's about you?"
  elif "Where do you live?" in user_input:
    return "I am the Chatbot,I don't have physical location."
  elif "What is your work?" in user_input:
    return "My work is to assist you,How can i help you today?"
  elif "Bye" in user_input:
    return "Good bye!,Have a great day!"
  else:
    return "I'm sorry ,I don't understand that."

while True:
  user_input= input("You:")
  # Remove the parentheses after user_input. You want to check the value, not call it.
  if user_input in ["Bye","Good bye"]:
    print("Chatbot: Goodbye! Have a great day!")
    break
  response= chatbot_response(user_input)
  print("Chatbot:",response)