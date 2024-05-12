from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

# from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter_demo import scrape_user_tweets
from third_parties.linkedin import scrape_gisthub_profile
from output_parsers import person_intel_parser, PersonIntel


def ice_break(name: str) -> PersonIntel:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    twitter_username = twitter_lookup_agent(name=name)

    linkedin_data = scrape_gisthub_profile(
        "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    )
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=5)

    summary_template = """
    given the Linkedin information {linkedin_information} and twitter {twitter_information} about a person 
    from I want you to create:
    1. a short summary
    2. two interesting facts about them
    3. A topic that may interest them
    4. 2 creative icebreakers to open a conversation with them
    \n {format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(linkedin_information=linkedin_data, twitter_information=tweets)
    return person_intel_parser.parse(result)


if __name__ == "__main__":
    print("Hello Langchain!")
    result = ice_break(name="Harrison Chase")
