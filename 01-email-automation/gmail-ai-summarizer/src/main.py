from summarizer import summarize_emails

def main():
    emails = [
        {
            "from": "boss@company.com",
            "subject": "Urgent meeting",
            "body": "We need to talk at 3pm today."
        },
        {
            "from": "hr@company.com",
            "subject": "Policy update",
            "body": "Please review the updated policy document."
        }
    ]

    summary = summarize_emails(emails)
    print(summary)   # 👈 THIS LINE WAS MISSING

if __name__ == "__main__":
    main()