import fanaa

while True:
    text = input("fana > ")
    result, error = fanaa.run("stdin", text)

    if error: print(error.as_string())
    elif result: print("Finished with Exit Code 0")

    
