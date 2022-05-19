import random

R_COMER = "I don't like eating anything because I'm a bot obviously!"
R_AVISO = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    resposta = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return resposta