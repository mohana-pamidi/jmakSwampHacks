import google.generativeai as genai

genai.configure(api_key="AIzaSyA6Z_GZ9sXgua6jcZm9JewLY8R-Io-Z1Tc")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text) #use response.txt and display to screen    
