from processor import process_email

# Define a "Stress Test" dataset
test_emails = [
    {
        "sub": "Invitation: Men's Day Celebration",
        "body": "Hi Sagar, join us for Men's day at 5 PM. Can you confirm?",
        "expected": "CAN IGNORE"
    },
    {
        "sub": "PROJECT CRITICAL: Server Down",
        "body": "The staging server is unresponsive. Need a fix by 2 PM.",
        "expected": "URGENT"
    },
    {
        "sub": "Quick Catchup?",
        "body": "Hey, do you have 15 mins tomorrow at 10 AM for a 1-on-1?",
        "expected": "SCHEDULING"
    },
    {
        "sub": "HR Policy Update",
        "body": "Please read the new remote work policy attached. No action needed.",
        "expected": "CAN IGNORE"
    }
]

print(f"{'SUBJECT':<30} | {'EXPECTED':<12} | {'ACTUAL':<12} | {'STATUS'}")
print("-" * 75)

for mail in test_emails:
    try:
        result = process_email(mail["sub"], mail["body"])
        status = "✅" if result.intent == mail["expected"] else "❌"
        
        print(f"{mail['sub'][:30]:<30} | {mail['expected']:<12} | {result.intent:<12} | {status}")
    except Exception as e:
        print(f"Error processing {mail['sub']}: {e}")