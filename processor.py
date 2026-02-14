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
    You are an Executive Mail Intelligence Agent. Your task is to analyze the provided email and extract structured data.

    --- 1. CATEGORIZATION RULES ---
    - URGENT: Direct work-related requests, specific deadlines, or blocking issues.
    - SCHEDULING: 1-on-1 meetings, interviews, or project syncs.
    - CAN IGNORE: Social events (e.g., Men's Day, Women's Day), office celebrations, generic HR broadcasts, or optional activities.

    --- 2. EXTRACTION RULES ---
    - sender_name: Extract from the signature or greeting (e.g., "Regards, Rahul").
    - key_question: The main request or question the sender is asking.
    - deadline: Any specific date or time mentioned (e.g., "by Friday", "at 5pm").
    - summary: A clear 2-sentence overview of the content.
    - --- PRIORITY KEYWORDS ---
    If you see these, it is likely SCHEDULING/URGENT, NOT social:
    - "1-on-1", "Sync", "Review", "Deadline", "Feedback", "Client".

    --- 3. FEW-SHOT EXAMPLES ---
    Example 1:
    Email: "Subject: Men's Day Celebration! Body: Join us for cake at 5pm. Can you confirm?"
    Result:
    {
    "intent": "CAN IGNORE",
    "summary": "Invitation to a Men's Day social celebration with cake.",
    "action_items": ["Confirm attendance"],
    "sender_name": "Unknown",
    "key_question": "Attend social event",
    "deadline": "5pm"
    }

    Example 2:
    Email: "Subject: Q1 Report. Body: Sagar, please send the PPT by tomorrow EOD. Thanks, Rahul."
    Result:
    {
    "intent": "URGENT",
    "summary": "Rahul is requesting the Q1 Report PPT by tomorrow end of day.",
    "action_items": ["Send PPT"],
    "sender_name": "Rahul",
    "key_question": "Send the Q1 PPT",
    "deadline": "Tomorrow EOD"
    }

    --- TASK ---
    Analyze the Subject and Body provided and generate the structured analysis.
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
# sample_sub = "Invting you to attend Men's day event"
# sample_body = "Hi Sagar, Inviting you to attend Men's day event 5 PM. Hope to see you there!"

# result = process_email(sample_sub, sample_body)
# print(f"Intent: {result.intent}")
# print(f"Action Items: {result.action_items}")