import google.generativeai as genai
from constants import *

class API:
    def __init__(self): 
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.response = None

    def makeAPICall(self, prompt):
        #we must send append prom
        self.response = self.model.generate_content(prompt)

    def getFeedBack(self):
        return self.response.text
    
    #returns integers between 0 and 10. 
    def getRating(self, feedback):
        index = self.response.text.find("/10")
        #self.response.text.split()
        pass
        #must parse feedback to get rating


        



