from processor import process_email
from replier import generate_draft

# Test with an URGENT email
sub = "URGENT: Need GitHub Access"
body = "Hi Sagar, can you grant me access to the repo by 4 PM today? Thanks, Amit."

# 1. Analyze
result = process_email(sub, body)

# 2. Generate Reply
draft = generate_draft(result)

# 3. Display
print(f"--- ANALYSIS ---")
print(f"Intent: {result.intent} | Sender: {result.sender_name} | Deadline: {result.deadline}")
print(f"\n--- SUGGESTED REPLY ---\n{draft}")