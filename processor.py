from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from utils import EmailAnalysis


# Initialize our local brain
llm = ChatOllama(model="llama3.2:1b", temperature=0)

# This is the 'Expert' magic: binding the model to the LLM
structured_llm = llm.with_structured_output(EmailAnalysis)

def process_email(subject, body):
    # 1. Define the instructions
    system_instructions = """
    You are an Executive Mail Classifier. You must categorize emails strictly based on these definitions:

    --- DEFINITIONS ---
    - URGENT: Work-related tasks with deadlines, direct requests from bosses/clients, or blocking issues.
    - SCHEDULING: 1-on-1 meetings, interviews, or project syncs.
    - CAN IGNORE: Generic HR broadcasts, social celebrations (e.g., Men's Day, Women's Day, Birthdays), newsletters, or optional office-wide events.

    --- CLASSIFICATION EXAMPLES ---
    Example 1: "Invitation: Men's Day Celebration at 5pm" -> CAN IGNORE (Reason: Social/HR event)
    Example 2: "Lunch on Friday?" -> CAN IGNORE (Reason: Social/Optional)
    Example 3: "Review the RAG report by EOD" -> URGENT (Reason: Work deadline)
    Example 4: "Sync regarding Project X tomorrow at 10am" -> SCHEDULING (Reason: Project meeting)
    More Examples: 
    1. Subject: 'Happy Women's Day', Body: 'Join us for cake at 4pm' -> CAN IGNORE
    2. Subject: 'Men's Day celebration', Body: 'Inviting you to attend at 5pm' -> CAN IGNORE
    3. Subject: 'Project Sync', Body: 'Can we meet at 5pm?' -> SCHEDULING   

    --- TASK ---
    Analyze the provided email and return the JSON. Even if a time (like 5 PM) is mentioned, if the event is social or generic HR, it MUST be CAN IGNORE.
    """
    
    email_content = f"Subject: {subject}\nBody: {body}"
    
    # 2. Create the message list
    messages = [
        SystemMessage(content=system_instructions),
        HumanMessage(content=email_content)
    ]
    
    # 3. Invoke with the full list of messages
    analysis = structured_llm.invoke(messages)
    return analysis

# --- Test Case ---
sample_sub = "Invting you to attend Men's day event"
sample_body = "Hi Sagar, Invting you to attend Men's day event 5 PM. Hope to see you there!"

result = process_email(sample_sub, sample_body)
print(f"Intent: {result.intent}")
print(f"Action Items: {result.action_items}")