import streamlit as st
import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    st.title("Rock Paper Scissors Game")
    st.write("Choose your move below:")
    
    if "user_score" not in st.session_state:
        st.session_state.user_score = 0
    if "computer_score" not in st.session_state:
        st.session_state.computer_score = 0
    
    user_choice = st.radio("Select one:", ["Rock", "Paper", "Scissors"], index=0)
    
    if st.button("Play"):
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == "You win!":
            st.session_state.user_score += 1
        elif result == "Computer wins!":
            st.session_state.computer_score += 1
        
        st.write(f"You chose: {user_choice}")
        st.write(f"Computer chose: {computer_choice}")
        st.success(result)
        
        st.write(f"**Your Score:** {st.session_state.user_score}")
        st.write(f"**Computer Score:** {st.session_state.computer_score}")

if __name__ == "__main__":
    main()
