from knowledge_base import  knowledge_base


def get_response(user_input):
    query = user_input.lower().strip()

    best_score = 0
    best_answer = None

    for keywords, response in knowledge_base:
        score = 0

        for keyword in keywords:
            keyword = keyword.lower()

            # Exact phrase match (strong signal)
            if keyword in query:
                score += 3
            else:
                # Partial word matching (weaker but useful)
                for word in keyword.split():
                    if word in query:
                        score += 1

        if score > best_score:
            best_score = score
            best_answer = response

    # If nothing meaningful matched
    if best_score == 0:
        return (
            "I couldn’t fully understand the issue. "
            "Try describing what’s happening, like what you expected vs what actually happened."
        )

    # Add human-like tone based on intent
    if "why" in query:
        return f"This usually happens because:\n\n{best_answer}"

    elif "how" in query:
        return f"Here’s how it generally works:\n\n{best_answer}"

    elif "fix" in query or "solve" in query:
        return f"To fix this issue:\n\n{best_answer}"

    else:
        return f"{best_answer}"
