from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


chatbot = ChatGroq(
    temperature=0,
    model="llama3-8b-8192"
)
system_message = "Please give a short answer to the user message"
with open('sysmsg.txt', 'r') as file:
     system_message = file.read()

prompt_template = ChatPromptTemplate.from_messages(
    [("system",system_message),("user","{user_input}")]
)

async def ask_bot(input):
    final_prompt = prompt_template.invoke({"user_input": input})
    response = chatbot.invoke(final_prompt)
    return(response.content)

def ask_bot_internal(input):
    final_prompt = prompt_template.invoke({"user_input": input})
    response = chatbot.invoke(final_prompt)
    return(response.content)


if __name__ == "__main__":
    personal_input = input("Ask any question: \n")
    print(ask_bot_internal(personal_input))
    
