import openai
import config
import typer
from rich import print 

def configure():
    openai.api_key = config.get_api_key()

def get_initial_context():
    messages = []
    user_name = typer.prompt("¿Cuál es tu nombre?\n") 
    user_country = typer.prompt("¿En qué país estás?\n") 
    messages.append({"role": "system", "content": "Eres un asistente para educación infantil en {}".format(user_country)})
    messages.append({"role": "system", "content": "Estas hablando con {}".format(user_name)})
    return messages

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

def get_user_topic():
    content = typer.prompt("\n¿Sobre qué quieres hablar? ")
    if is_bye_message(content):
        is_exit = typer.confirm("¿Quieres terminar nuestra conversación?")
        if is_exit:
            print("\n[green]Ha sido un placer conversar contigo.  Hasta la próxima[/green] 👋🏽\n")
            raise typer.Abort()
        else:
            return get_user_topic()

    return content

def welcome_message():
    print("\n[green bold][u]Aprendamos juntos[/u][/green bold]\n\n")

def main():
    configure()
    welcome_message()
    is_active = True
    messages = get_initial_context()

    print("\n👉🏽 [green]Escribe exit cuando quieras terminar la conversación[/green]\n")

    while is_active:
        content = get_user_topic()
        message = {"role": "user", "content": content}
        
        messages.append(message)
        response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages = messages)
        
        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green][green]{response_content}[/green]")

if __name__ == '__main__':
    typer.run(main)