def greet(name, lang="en"):
    if lang.lower() == "en":
        print("Hello", name)
    elif lang.lower() =="fr":
        print("Bonjour", name)
    elif lang.lower() == "esp":
        print("Hola", name)
    elif lang.lower() == "grm":
        print("Halo", name)
    else: 
        print("Language unrecognized")

greet("Oussama")
greet("Oussama", "fr")
greet("Oussama", "grm")
greet("Oussama", "arb")
