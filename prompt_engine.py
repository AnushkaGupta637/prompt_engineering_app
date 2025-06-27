#library for generative ai
import google.generativeai as genai

#configuring gemeini api key
gemini_api_key = "AIzaSyBz2cGL2NABblf_xxRCoUPXEfhBlWPi6jo"
genai.configure(api_key = gemini_api_key)

model = genai.GenerativeModel("models/gemini-2.0-flash-001")

#create a function to define the prompts
def run_prompt(prompt_type,user_input):
    if prompt_type =="Zero-Shot":
        prompt = f"{user_input}"

    elif prompt_type =="Few-Shot":
        prompt = (
            "Q: who is the president of india\n\n"
            "A: Ms. Draupadi Murmu"
            "Q: who is the President of United State\n\n"
            "A: Mr. Donald Trump"
            f"Q:{user_input}\n"
            "A: "
        )
    
    elif prompt_type=="Instruction-Based":
        prompt =(
            "Instruction: Summerize my article in 3 bullet points"
            f"Text: {user_input}" 
        )

    elif prompt_type=="Chain-of-Thought":
        prompt = (
            "Solve the Neural network backpropogation equation step by step"
            f"Text:{user_input}"
        )
    
    elif prompt_type =="Role-based":
        prompt =(
            "You are a real estate consultant, pls tell me why should i purchase a property in Gurgaon"
            f"text:{user_input}"
        )
    else:
        prompt =user_input

    response = model.generate_content(prompt)
    return response.text.strip()