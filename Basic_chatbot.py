def chatbot():
  print("Chatbot: Hello! Type something to start the conversation.")
  while True:
    user_input = input("You:").lower()
    if user_input == "hello":
      print("Chatbot: Hi!")
    elif user_input == "how are you":
      print("Chatbot: I'm fine")
    elif user_input == "bye":
      print("Chatbot: Goodbye!")
      break
    else:
      print("Chatbot: Sorry, I don't understand that.")
