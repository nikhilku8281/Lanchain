from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from third_parties.linkedin import scrape_gisthub_profile
from third_parties.twitter_demo import scrape_user_tweets
from agents.linkedin_lookup_agent import lookup

information = """
    Narendra Modi
"""

if __name__ == "__main__":
    print("Hello Langchain ")

    # function to call linkedin profile
    # linkedin_profile_url = lookup("Nikhil Kumar Senior Product manager Thomson reuters Canada")

    # summary_template = """
    #     given the LinkedIn information {information} about a person from what I want you to create:
    #     1. a short summary
    #     2. two interesting facts about them
    # """
    # summary_promt_template = PromptTemplate(
    #     input_variables=["information"], template=summary_template
    # )
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # chain = LLMChain(llm=llm, prompt=summary_promt_template)
    # ## Below code to be used at time of using Linkedin API
    # # linkedin_data=scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/harrison-chase-961287118')
    #
    #
    # ## Below code to be used at time when calling a Linkedin function by supplying only name
    #
    # #linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    #
    # #print(chain.run(information=linkedin_data))
    # gisthub = scrape_gisthub_profile(
    #     "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    # )
    # print(chain.run(information=gisthub))
    print(scrape_user_tweets(username="elonmusk", num_tweets=20))
