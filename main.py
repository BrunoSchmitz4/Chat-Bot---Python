import re
import long_response as long


def message_probability(mensagem_usuário, palavras_reconhecidas, resposta_unica =False, palavras_requisitadas=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in mensagem_usuário:
        if word in palavras_reconhecidas:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(palavras_reconhecidas))

    # Checks that the required words are in the string
    for word in palavras_requisitadas:
        if word not in mensagem_usuário:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or resposta_unica:
        return int(percentage * 100)
    else:
        return 0


def checar_todas_menssagens(menssagem):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def resposta(bot_response, lista_de_palavras, resposta_unica = False, palavras_requisitadas=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(menssagem, lista_de_palavras, resposta_unica, palavras_requisitadas)

    # Responses -------------------------------------------------------------------------------------------------------
    resposta('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], resposta_unica=True)
    resposta('See you!', ['bye', 'goodbye'], resposta_unica=True)
    resposta('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], palavras_requisitadas=['how'])
    resposta('You\'re welcome!', ['thank', 'thanks'], resposta_unica=True)
    resposta('Thank you!', ['i', 'love', 'code', 'palace'], palavras_requisitadas=['code', 'palace'])

    # Longer responses
    resposta(long.R_AVISO, ['give', 'advice'], palavras_requisitadas=['advice'])
    resposta(long.COMER, ['what', 'you', 'eat'], palavras_requisitadas=['you', 'eat'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match




# Used to get the response
def get_resposta(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = checar_todas_menssagens(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_resposta(input('You: ')))