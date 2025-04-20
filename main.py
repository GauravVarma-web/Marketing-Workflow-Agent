# main.py
import os
from dotenv import load_dotenv
from actions import analyze_campaign_data, generate_content, schedule_content
from prompts import workflow_system_prompt
from json_helpers import extract_json
from openai import OpenAI  # Make sure this import is correct

# Load environment variables
load_dotenv()

# Set up OpenAI client (create an instance of the client)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Available actions
available_actions = {
    "analyze_campaign_data": analyze_campaign_data,
    "generate_content": generate_content,
    "schedule_content": schedule_content
}

def generate_response(messages, model="gpt-3.5-turbo"):
    """Generate a response from the language model"""
    response = client.chat.completions.create(  # Use the client instance
        model=model,
        messages=messages
    )
    return response.choices[0].message.content

def run_workflow_agent():
    """Run the Marketing Workflow Agent"""
    print("\n=== Marketing Workflow Agent ===")
    print("This agent can analyze campaigns, generate content, and schedule posts.")
    print("Type 'exit' to quit.\n")
    
    # Initialize conversation with system prompt
    messages = [
        {"role": "system", "content": workflow_system_prompt}
    ]
    
    while True:
        # Get user input
        user_input = input("\nWhat marketing task can I help you with? ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Add user input to messages
        messages.append({"role": "user", "content": user_input})
        
        # Initialize loop variables
        turn_count = 1
        max_turns = 5
        
        # Agent loop
        while turn_count < max_turns:
            print(f"\n[Thinking... Step {turn_count}/{max_turns}]")
            
            # Get response from language model
            ai_response = generate_response(messages)
            print(f"\nWorkflow Agent: {ai_response}")
            
            # Check if we need to execute an action
            json_function = extract_json(ai_response)
            
            if json_function:
                # We found a function call
                function_name = json_function[0]['function_name']
                function_parms = json_function[0]['function_parms']
                
                # Check if function exists
                if function_name not in available_actions:
                    print(f"Error: Unknown action '{function_name}'")
                    break
                
                # Execute the function
                print(f"\n[Executing {function_name}...]")
                action_function = available_actions[function_name]
                result = action_function(**function_parms)
                
                # Format the result
                function_result_message = f"Action_Response: {result}"
                print(f"\n[Result: {function_result_message}]")
                
                # Add messages to conversation
                messages.append({"role": "assistant", "content": ai_response})
                messages.append({"role": "user", "content": function_result_message})
                
                turn_count += 1
            else:
                # No function call, we're done
                messages.append({"role": "assistant", "content": ai_response})
                break

if __name__ == "__main__":
    run_workflow_agent()