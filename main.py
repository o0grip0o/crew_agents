import os

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "NA"

class MathProfessor():

    def __init__(self):
        self.llm = self.get_llm()

    def get_llm(self):
        llm = ChatOpenAI(
            model="crewai-llama",
            base_url="http://localhost:11434/v1",
        )
        return llm

    def agent(self, llm: ChatOpenAI) -> str:
        general_agent = Agent(role="Math Professor",
                                goal="""Provide the solution to the students that are asking mathematical questions and give them the answer.""",
                                backstory="""You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
                                allow_delegation=False,
                                verbose=True,
                                llm=llm)
        task = Task(description="""Explain why you can't divide by zero""",
                    agent=general_agent,
                    expected_output="""response will be a detailed explanation of why you can't divide by zero and must include a discrete math proof.""")
        crew = Crew(
            agents=[general_agent],
            tasks=[task],
            verbose=4
        )
        result = crew.kickoff()
        return result

        result = agent(llm)
        return(result)

def main():
    math_professor = MathProfessor()
    llm = math_professor.llm
    result = math_professor.agent(llm)
    print(result)

if __name__ == "__main__":
    main()