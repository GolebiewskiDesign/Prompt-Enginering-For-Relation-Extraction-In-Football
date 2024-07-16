import os
import warnings
from langchain.llms import OpenAI
# One Shot Example
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
import pandas as pd
import numpy as np
import spacy
from dotenv import load_dotenv
from spacy import displacy
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st
import scipy
import plotly_express as px
from pyvis.network import Network
import community as community_louvain




warnings.filterwarnings("ignore", category=DeprecationWarning)
os.environ["OPENAI_API_KEY"] = "sk-proj-8ECIx8QFAMKiQixAMfecT3BlbkFJNW9b2n1pvHtO6v6EV6TQ"   #os.getenv("OPENAI_API_KEY")

# Zero Shot Example
llm = OpenAI(temperature=0.7)
text= "Kylian Mbappe"

print(llm(text))


# One Shot Prompt
example = [
    {"Player": "Robert Lewandowski",
     "History": "Robert Lewandowski (born 21 August 1988) is a Polish professional footballer who plays as a striker for La Liga club Barcelona and captains the Poland national team. He is regarded as one of the best players of his generation and as one of the best strikers of all time, as well as the most successful player in Bundesliga and Bayern Munich history. He has scored over 600 senior career goals for club and country."
     }
]

example_prompt = PromptTemplate(
    input_variables=["Player", "History"],
    template="Player: {Player}\n {History}"
)

print(example_prompt.format(**example[0]))

prompt = FewShotPromptTemplate(
    examples =example,
    example_prompt=example_prompt,
    suffix="Player: {input}",
    input_variables= ["input"]
)

print(llm(prompt.format(input="Andrea Pirlo")))



# Few Shot Prompting
examples = [
    {"Player": "Robert Lewandowski",
     "History": "Robert Lewandowski (born 21 August 1988) is a Polish professional footballer who plays as a striker for La Liga club Barcelona and captains the Poland national team. He is regarded as one of the best players of his generation and as one of the best strikers of all time, as well as the most successful player in Bundesliga and Bayern Munich history. He has scored over 600 senior career goals for club and country."
     },
    {
        "Player":"Francesco Totti",
        "History": "Francesco Totti ( Rome , 27 September 1976 ) is a former Italian footballer , who played as a forward or midfielder . With the Italian national team he became world champion in 2006 and European runner-up in 2000 .Considered one of the best Italian players of all time as well as one of the strongest in the world of his generation,  throughout his competitive career he has always played for Roma , the team of which he was captain from 1998  to 2017, for a record total of 19 seasons,  winning one Scudetto ( 2000-2001 , the third in the Giallorossi's history ), two Italian Super Cups ( 2001 and 2007 ) and two Italian Cups ( 2006-2007 and 2007-2008 )."
    },
    {
        "Player": "Paulo Dybala",
        "History": "Paulo Dybala (born 15 November 1993) is an Argentine footballer who plays as a forward for Italian club Roma and the Argentina national team. He began his career as a professional footballer in 2011 in the Argentine Second division. In 2012, he moved to Europe and signed for Palermo. His great performances in Serie A got him a transfer to Juventus in 2015. Due to his creative style of play, pace, technique, talent, and eye for goal, he has been nicknamed La Joya (The Jewel in Spanish.)"
    }
]

example_prompt = PromptTemplate(
    input_variables=["Player", "History"],
    template="Player: {Player}\n {History}"
)

prompt = FewShotPromptTemplate(
    examples =examples,
    example_prompt=example_prompt,
    suffix="Player: {input}",
    input_variables= ["input"]
)

print(prompt.format(input="Andrea Pirlo"))


# Generate few shot examples
few_shot_example1 = llm(prompt.format(input="Paulo Dybala"))
print(few_shot_example1)

few_shot_example2 = llm(prompt.format(input="Robert Lewandowski"))

print(few_shot_example2)

few_shot_example3 = llm(prompt.format(input="Cristiano Ronaldo"))
print(few_shot_example3)

few_shot_example4 = llm(prompt.format(input="Michael Jordan"))
print(few_shot_example4)



# Relation extraction

#Load the model
nlp= spacy.load('en_core_web_md')

data = few_shot_example1+few_shot_example2+few_shot_example3+few_shot_example4
doc= nlp(data)


# Prepare doc objects from raw text
doc_1 = nlp(few_shot_example1)
doc_2 = nlp(few_shot_example2)
doc_3 = nlp(few_shot_example3)
doc_4 = nlp(few_shot_example4)

displacy.render(doc_1,style="ent",jupyter=True)


# Create global variable (e.g to append entities to list, and to store relationships)
image=0 # This variable will be used to store an image
all_entities = []
relationships = []
new_entity_list = []
relationships_df = pd.DataFrame()
source_code=""
node_degree=""
third_graph=""

# Get entities from each sentence of a text

def get_entities(doc):
  for sent in doc.sents:
    entity = [ent.text for ent in sent.ents]
    all_entities.append({"entities":entity})
  print(all_entities)


# Create dataframe based on entities and create relationships between them
def create_relationships():
  # Create a dataframe
  all_entities_dataframe = pd.DataFrame(all_entities)
  # Filter out sentences that don't have any entities
  all_entities_dataframe = all_entities_dataframe[all_entities_dataframe["entities"].str.len() > 0]
  print(all_entities_dataframe.head())

  # Create relationships
  entity_list = []

  for i in range (all_entities_dataframe.index[-1]):
    end = min(i+1, all_entities_dataframe.index[-1]) # to not go out of range
    entity_list = sum((all_entities_dataframe.loc[i:end].entities),[])
    new_entity_list.append(entity_list)
    print(entity_list)

  # Remove duplicated entites
    entity_list_original = [entity_list[i] for i in range(len(entity_list))
                          if(i==0) or (entity_list[i] != entity_list[i-1])]
    if len(entity_list_original)>1:
      for index, a in enumerate(entity_list_original[:-1]):
        b = entity_list_original[index+1]
        relationships.append({"source":a, "target":b})



def dataframe_visualization():
  # pd.set_option('display.max_rows',None)
  # relationships_df
  relationships_df = pd.DataFrame(relationships)
  # Search for duplications
  relationships_df = pd.DataFrame(np.sort(relationships_df.values,axis=1), columns=relationships_df.columns)

  # Create a value to monitor how many times relationships appears
  relationships_df['value']=1
  relationships_df = relationships_df.groupby(['source','target'],sort=False, as_index=False).sum()

  # Check how many this relationships appear in a text
  print(relationships_df)
  return relationships_df



def graph_visualization():
  # Create a Graph from dataframe
  graph = nx.from_pandas_edgelist(relationships_df, source='source', target='target', edge_attr='value', create_using=nx.Graph())
  # Graph Visualization
  plt.figure(figsize=(25,25))
  pos = nx.kamada_kawai_layout(graph)
  nx.draw(graph,with_labels=True, node_color='lightgreen',  pos=pos)
  plt.savefig("plot.jpg", dpi=100)
  plt.show()
  net = Network(notebook=False, width="1000px",height="700px",bgcolor="#222222",font_color="white")
  node_degree = dict(graph.degree)
  # Set node size
  nx.set_node_attributes(graph, node_degree, 'size')
  net.from_nx(graph)
  net.save_graph('graph.html')
  # Community detection
  communities = community_louvain.best_partition(graph)
  nx.set_node_attributes(graph,communities,'group')
  com_net = Network(notebook=False, width="1000px",height="700px",bgcolor="#222222",font_color="white")
  com_net.from_nx(graph)
  com_net.save_graph('graph_2.html')

relationships = []
relationships_df = pd.DataFrame()



# Visualization using streamlit
html_element_1 = '''
<h2 class="header_Title">Web Mining and Retrieval - Project for 9 CFU</h2>'''
html_element_2='''
<h2 class="header_Title">Author: Kacper Gołębiewski</h2>
'''
html_element_3='''
<h2 class="header_Title">Topic: Prompt Engineering for Relation Extraction (in football)</h2>
'''
css_element = """
<style>
.header_Title{
    align-text:center;
    align-self: center;
    font-size: 25px;
    background: linear-gradient(45deg,transparent,#1c95c56d,transparent); 
    color: white;
    border-radius: 10px;
    padding: 0.3rem 0.3rem;
    background-size: 5px;
    text-decoration: line-through;
    text-decoration-color: #1c95c525;
    text-decoration-thickness: 20px;
    animation: slow 8s ease forwards;
    white-space: nowrap;
    overflow: hidden;
}
.documentation__Header__Title:active
{
    text-decoration: none;
}
.documentation__Header__Title::selection
{
    color:black;
}
@keyframes slow 
{
    from 
    {
      max-width: 0rem;
    }
    to 
    {
      max-width: 50rem;
    }
}
"""

st.write(css_element,unsafe_allow_html=True)
st.write(html_element_1,unsafe_allow_html=True)
st.write(html_element_2,unsafe_allow_html=True)
st.write(html_element_3,unsafe_allow_html=True)
st.write("Hello, write the name and surname of sport player below (e.g. Paulo Dybala): ")
# Create a form for user
form = st.form(key="form")
player = form.text_input("Name and surname")
submit = form.form_submit_button(label="Submit the Player")

if player:
    st.write(f"Player you choose is: {player}")
    st.title("1. Relation Extraction")
    player_few_shot = llm(prompt.format(input=player))
    player_doc = nlp(player_few_shot)
    entites= get_entities(player_doc) # Get all entities (they will be stored in all_entities list) for doc object 1, to create relationships
    print("NEXT STEP")
    create_relationships()
    print("NEXT STEP")
    relationships_df=dataframe_visualization()
    print("NEXT STEP")
    graph_visualization()
    # Show first graph
    st.image("plot.jpg", caption="Player Plot")
      # Read HTML file, with a graph
    with open("graph.html", 'r', encoding='utf-8') as f:
        source_code = f.read()
    # Show second graph
    st.components.v1.html(source_code, height=500, width=500, scrolling=True)
    st.write(node_degree)
    #Show third graph
    with open("graph_2.html", 'r', encoding='utf-8') as f:
        third_graph = f.read()
    st.components.v1.html(third_graph,height=500, width=500, scrolling=True)

    # To download the image:
    with open("plot.jpg","rb") as file:
     btn=st.download_button(
        label="Download Player Relation",
        data=file,
        file_name="playerRelation.png",
        mime="image/png"
        )
    st.title(f"2. History of {player}")
    st.write(player_few_shot)
    
    st.title(f"3. Dataframe of relations ")
    st.write(relationships_df)
    st.write(f"All the entities in each sentence: {new_entity_list}")
    st.line_chart(relationships_df)
    st.bar_chart(relationships_df)
