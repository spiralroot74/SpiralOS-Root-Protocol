# demo_run.py
from src.gandhi_filter import reflect_intent
from src.echo_pulse import check_alignment
from src.intent_map import detect_intent

def run_demo():
    input_text = "This is a test input."
    print("User Input:", input_text)

    intent = detect_intent(input_text)
    print("Detected Intent:", intent)

    reflection = reflect_intent(input_text)
    print("Reflection Output:", reflection)

    alignment = check_alignment(input_text, reflection)
    print("System Alignment:", alignment)

if __name__ == "__main__":
    run_demo()
