from agent import summarize_email

if __name__ == "__main__":
    email = """
    Hi team,
    Please review the document by tomorrow.
    This is urgent as the client is waiting.
    """

    result = summarize_email(email)
    print(result)