import streamlit as st

def main():
    st.title("Welcome to our Intelligent Bot Platform!👋")

    st.markdown(
        """
        Hello there, dear friend! Welcome to our innovative platform where cutting-edge technology meets user-friendly solutions. 
        We're thrilled to have you here as we introduce you to three powerful features that will transform the way you interact with information – our Q&A Bot, Text Summarization Bot, and Image Recognition Bot.
        """
    )

    st.subheader("🤖Q&A tool: Unlocking Knowledge with Ease")
    st.write(
        "Say goodbye to endless searches and information overload. Our Q&A Bot is designed to simplify your quest for knowledge. "
        "Just ask a question, and let our intelligent bot scour the web to provide you with accurate and relevant answers. "
        "Whether you're a student, a professional, or just curious, our Q&A Bot is your go-to companion for instant information retrieval."
    )

    st.subheader("🔍Text Summarization tool: Condense Complexity, Embrace Simplicity")
    st.write(
        "In a world filled with information, the ability to distill key insights is invaluable. Our Text Summarization Bot does just that – "
        "it takes lengthy articles, documents, or paragraphs and condenses them into clear and concise summaries. "
        "Save time, stay informed, and grasp the essence of content effortlessly with this feature."
    )

    st.subheader("🔆Image Recognition tool: Seeing the World in a New Light")
    st.write(
        "A picture is worth a thousand words, and our Image Recognition Bot takes this to a whole new level. "
        "Upload an image, and watch as our bot identifies objects, landmarks, and even provides contextual information. "
        "Whether you're a photography enthusiast or someone looking to extract details from images, our Image Recognition Bot is here to add a visual dimension to your exploration."
    )

    st.write(
        "Ready to embark on a journey of seamless information discovery? Dive into the world of possibilities with our three exceptional bots. "
        "Empower yourself with quick answers, concise summaries, and visual insights – all at your fingertips. Your digital companion awaits you. Let's explore, learn, and simplify together!"
    )

if __name__ == "__main__":
    main()
