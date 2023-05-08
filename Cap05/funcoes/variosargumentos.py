def elementos(primeiro, *args):
    print(f"Olá amigo, {primeiro}")

    if args:
        for i in args:
            print(f"Olá amigo, {i}")
    return


elementos("Jacob")
elementos("Jacob", "Mario", "Igão", "Marcos")
