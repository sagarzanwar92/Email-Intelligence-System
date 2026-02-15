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



def extract_writing_style(sample_emails):
    analysis_prompt = """
    Analyze these emails and identify the writing style. Look for:
    1. Greeting style (e.g., 'Hi [Name],', 'Hey!', or no greeting?)
    2. Sentence length (Short/punchy or long/detailed?)
    3. Closing (e.g., 'Regards, Sagar', 'Best, S', 'Cheers!')
    4. Use of emojis or specific industry jargon.

    Respond with ONLY 5-10 bullet points describing the 'Voice'.
    """
    # (Standard LLM invoke logic here...)
    return style_bullet_points