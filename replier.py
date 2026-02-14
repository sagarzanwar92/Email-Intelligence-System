def generate_draft(analysis):
    # Strategy 1: The Professional Decline
    if analysis.intent == "CAN IGNORE":
        return (f"Hi {analysis.sender_name},\n\n"
                f"Thanks for the invite regarding '{analysis.key_question}'! "
                "I won't be able to make it this time, but I hope it's a great event.\n\n"
                "Best,\nSagar")

    # Strategy 2: The Action-Oriented Response
    elif analysis.intent == "URGENT":
        deadline_text = f" by {analysis.deadline}" if analysis.deadline != "None" else ""
        return (f"Hi {analysis.sender_name},\n\n"
                f"I've received your request regarding '{analysis.key_question}'. "
                f"I'm prioritizing this and aim to have it resolved{deadline_text}.\n\n"
                "Regards,\nSagar")

    # Strategy 3: The Meeting Confirmation
    elif analysis.intent == "SCHEDULING":
        return (f"Hi {analysis.sender_name},\n\n"
                f"I'd be happy to sync regarding '{analysis.key_question}'. "
                f"The proposed time ({analysis.deadline}) works for me. Looking forward to it.\n\n"
                "Best,\nSagar")

    return "Draft could not be generated."