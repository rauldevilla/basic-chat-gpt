import openai
import config

openai.api_key = config.api_key

def get_initial_context():
    messages = []
    user_name = input("¿Cuál es tu nombre?\n> ") 
    user_country = input("En qué país estás?\n> ") 
    messages.append({"role": "system", "content": "Eres un asistente para educación infantil en {}".format(user_country)})
    messages.append({"role": "system", "content": "Estas hablando con {}".format(user_name)})
    return messages

def get_user_question():
    content = input("\n¿Qué quieres saber?\n> ")
    return {"role": "user", "content": content}

def is_bye_message(message_text):
    evaluation_message = message_text.strip().upper()
    return  evaluation_message == 'BYE' or \
            evaluation_message == 'CHAO' or \
            evaluation_message == 'CHAITO' or \
            evaluation_message == 'HASTA MAÑANA' or \
            evaluation_message == 'QUIT' or \
            evaluation_message == 'EXIT' or \
            evaluation_message == 'ME VOY' or \
            evaluation_message == 'YO YA ME VOY'

def main():
    is_active = True
    messages = get_initial_context()
    while is_active:
        user_question = get_user_question()
        is_active = not is_bye_message(user_question['content'])
        if is_active:
            messages.append(user_question)
            response = openai.ChatCompletion.create(
                        model = "gpt-3.5-turbo",
                        messages = messages)
            print(response.choices[0].message.content)
        else:
            print("\nHa sido un placer haber conversado contigo. Nos hablamos luego !\n")

main()