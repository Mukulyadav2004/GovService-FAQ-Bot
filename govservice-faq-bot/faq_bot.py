import json
import random
import time

# These functions pretend to get live data, but really just give random or fixed answers
# In a real project, these would connect to real websites or APIs

def get_processing_time():
  """Simulates fetching the current passport processing time."""
  # This would be a delay if we were really waiting for a website
  # time.sleep(0.5)
  # Pick a random number of weeks for fun
  return random.choice([3, 4, 5, 6])

def get_passport_fee():
  """Simulates fetching the current passport application fee."""
   # This would be a delay if we were really waiting for a website
  # time.sleep(0.3)
  return 1500 # This is just a made-up fee in INR

# This connects the names in the FAQ file to the pretend functions above
DYNAMIC_DATA_FUNCTIONS = {
    "get_processing_time": get_processing_time,
    "get_passport_fee": get_passport_fee,
}


def load_faqs(filepath="faqs.json"):
  """Loads keywords and responses from the JSON file."""
  try:
    with open(filepath, 'r') as f:
      data = json.load(f)
    return data['keywords'], data['responses'], data.get('dynamic_data_providers', {})
  except FileNotFoundError:
    print(f"Error: FAQ file not found at {filepath}")
    return None, None, None
  except json.JSONDecodeError:
    print(f"Error: Could not parse JSON file at {filepath}")
    return None, None, None

def find_answer(query, keywords, responses, dynamic_providers):
  """
    Processes the user query, finds relevant keywords, fetches static
    or dynamic responses, and formats the answer.
  """
  query_lower = query.lower()
  matched_response_key = None

  # Look for the longest keyword first, so we match more specific things
  sorted_keywords = sorted(keywords.items(), key=lambda x: len(x[0]), reverse=True)
  for keyword, response_key in sorted_keywords:
    if keyword in query_lower:
      matched_response_key = response_key
      break

  if matched_response_key:
    answer_template = responses.get(matched_response_key)
    if not answer_template:
      return responses.get("default", "Sorry, I encountered an error.")

    # Check if this response needs dynamic data
    dynamic_data = {}
    provider_function_name = dynamic_providers.get(matched_response_key)

    if provider_function_name and provider_function_name in DYNAMIC_DATA_FUNCTIONS:
      print(f"[Simulating API call for {matched_response_key}...]")
      dynamic_value = DYNAMIC_DATA_FUNCTIONS[provider_function_name]()
      # Determine the placeholder key based on the response key (e.g., passport_time -> processing_time)
      placeholder_key = matched_response_key.split('_')[-1] # Simple heuristic
      if matched_response_key == "passport_time": placeholder_key = "processing_time" # Explicit mapping
      if matched_response_key == "passport_cost": placeholder_key = "passport_fee"   # Explicit mapping

      dynamic_data[placeholder_key] = dynamic_value

    # Format the answer using the template and any dynamic data
    try:
      formatted_answer = answer_template.format(**dynamic_data)
      return formatted_answer
    except KeyError as e:
      print(f"[Warning] Mismatch between response template placeholder and dynamic data key: {e}")
      # Return template without formatting if key is missing
      return answer_template
    except Exception as e:
        print(f"[Error] Could not format answer: {e}")
        return responses.get("default", "Sorry, I encountered an formatting error.")


  else:
    # No keyword matched
    return responses.get("default", "Sorry, I don't understand. Can you rephrase?")


def main():
  """Main function to run the FAQ bot."""
  keywords, responses, dynamic_providers = load_faqs()

  if keywords is None or responses is None:
    print("Exiting due to FAQ loading error.")
    return

  print("Welcome to the GovService FAQ Bot (Passport Info)!")
  print("Ask me about passport application, status, cost, processing time, or required documents.")
  print("Type 'quit' to exit.")

  while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'quit':
      print("Bot: Goodbye!")
      break

    answer = find_answer(user_input, keywords, responses, dynamic_providers)
    print(f"Bot: {answer}")

if __name__ == "__main__":
  main()