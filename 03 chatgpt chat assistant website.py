import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Create a trip planner itinerary from the place of visit,start date and end date given by the userand  also make it funny.Here is an example for you :Day 1 - April 2nd:Explore Fort Kochi: visit St. Francis Church and see the Chinese fishing nets (don't worry, you won't have to catch any fish yourself!).Walk along the seaside promenade and try not to get sprayed by the waves (or the sneaky local vendors trying to sell you things).Attend a traditional Kathakali dance performance at the Kathakali Centre, and try not to fall asleep during the slow parts (trust us, it's worth it for the colorful makeup and costumes!).Day 2 - April 3rd:Take a boat ride to Mattancherry Island and visit the Mattancherry Palace, where you can pretend you're a royal for the day (just don't let it go to your head!).Walk through Jew Town and try to haggle for a good deal on some souvenirs (bonus points if you can convince the shop owner to throw in a free chai).Visit the Paradesi Synagogue and marvel at the beautiful blue and white tiles (just don't accidentally break any!). Explain in detail about the places to visit"}]

def CustomChatGPT(Destination):
                      
    messages.append({"role": "user", "content": Destination})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = [gradio.inputs.Textbox(label="Enter Destination,Start Date and End Date of the Journey:")], outputs = [gradio.inputs.Textbox(label="Your Travel Plan:")], title = "Easy Trip")

demo.launch(share=True)
