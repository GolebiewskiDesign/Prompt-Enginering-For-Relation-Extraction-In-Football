# This file is based on HTML + CSS + JavaScript
import streamlit as st
html_element_1 = '''
<h1 class="header_Title">Documentation of Relation Extraction Project in Sports</h1>'''

html_element_2='''
<h2>1. Goal of the Project </h2>
'''
html_element_3='''
<h3>Objective</h3>
<p>The project focuses on leveraging prompt engineering for relation extraction in the context of sports players' biographies. The primary goal is to demonstrate how natural language processing (NLP) and machine learning models can be utilized to extract meaningful relationships and entities from text, visualize these relationships, and provide insights into the biographies of sports players.</p>
<h3>Rationale</h3>
<p>Relation extraction is a pivotal task in NLP, enabling the identification of connections between entities within text. This project aspires to demonstrate how prompt engineering—specifically through few-shot methodology, can enhance the precision and efficiency of relation extraction. By doing so, it provides a potent instrument for deciphering complex information embedded within text, thereby facilitating the analysis and visualization of inter-entity relationships.</p>
'''

html_element_4='''
<h2>2. Application Usage</h2>
<p><strong>Streamlit Interface: </strong> The application is constructed using Streamlit, offering an intuitive and interactive interface for user data input and result visualization.</p>
<p><strong>Input Player Name:</strong> Users are invited to input the name and surname of a sports player (e.g., Paulo Dybala) into the provided text field and submit the entry.</p>
<p><strong>Biography creation: </strong>The application employs an OpenAI language model to generate an extensive biography of the player based on few-shot prompting techniques. This generated text is subsequently processed using SpaCy for entity recognition.</p>
<p><strong>Relationship Creation:</strong>The application constructs relationships between the recognized entities and stores them in a dataframe for subsequent analysis.</p>
<p><strong>Graph Visualization:</strong>he relationships are visualized using NetworkX and PyVis, creating interactive graphs that depict the connections between entities.</p>
<p><strong>Community Detection:</strong>The application performs community detection to identify clusters of related entities, providing deeper insights into the structure of the relationships.</p>
<p><strong>Data Analysis:</strong>: The application presents the extracted relationships and entities in various formats, including dataframes, line charts, and bar charts, to facilitate comprehensive analysis.</p>
'''

html_element_5='''
<h2>3. Code Analysis</h2>
<h3>Imports and Environment Setup</h3>
'''

html_image_1='''
<img src="images/enviromentsetup.png" alt="Enviroment Setup Image" >
'''

html_element_6='''
<p><strong>langchain</strong> for handling large language models and prompts.</p>
<p><strong>pandas and numpy</strong> for data manipulation and analysis.</p>
<p><strong>spacy</strong>  for NLP tasks, including named entity recognition (NER)..</p>
<p><strong>networkx and pyvis</strong>  for network visualization.</p>
<p><strong>streamlit</strong> for creating a web application interface.</p>
<p><strong>matplotlib and plotly_express</strong> for plotting.</p>
<p><strong>community</strong> for community detection in graphs.</p>
'''

html_element_7='''
<h3>Relation Extraction</h3>
<p>The subsequent part involves extracting relationships from the generated biographies using spacy.</p>
'''

html_element_8='''
<h2> 4. Project Summary: Web Mining and Retrieval for Relation Extraction in Sports</h2>
<p>This project leverages advanced Natural Language Processing (NLP) techniques and interactive data visualization tools to extract and visualize relationships between entities within textual descriptions of sports players. The primary objective is to utilize prompt engineering to generate comprehensive historical data for various athletes and represent the inter-relationships among entities in an engaging and informative manner.</p>
<p>This project demonstrates the powerful combination of NLP and data visualization in extracting and presenting complex relationships within text data. By offering an intuitive and interactive platform, it allows users to gain deep insights into the histories and connections of sports players, making it a valuable tool for sports analysts, enthusiasts, and researchers.</p>
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
st.write(html_element_4,unsafe_allow_html=True)
st.write(html_element_5,unsafe_allow_html=True)
st.image('images/enviromentsetup.png',caption='Enviroment Setup')
st.write('Library Imports: The script imports various libraries to handle natural language processing (NLP), data manipulation, and visualization. Key libraries include:')
st.write(html_element_6,unsafe_allow_html=True)

st.write('Provide Your api key  in .env file to run a project from this website: https://platform.openai.com/settings/profile?tab=api-keys')
st.image('images/openai_api_key.png',caption='Provide Your Own API key in .env file')
st.write('Zero-Shot Example: This segment initializes an instance of the OpenAI language model with a specified temperature setting, which controls the randomness of the models outputs. A zero-shot prompt is used to generate text about "Kylian Mbappe"')
st.image('images/zero_shot_example.png',caption='Zero Shot Example')
st.image('images/mbappe_example.png',caption='Mbappe Result - Zero Shot Prompt')
st.write('One-Shot Example: This section illustrates the creation of a one-shot prompt using PromptTemplate, where a pre-formulated example of Robert Lewandowski biography is provided. This serves as a template for generating similar structured outputs for other inputs.')
st.image('images/one_shot_example.png',caption='One Shot Example')
st.image('images/lewandowski_example.png',caption='Robert Lewandowski - One Shot Prompt')
st.write('Few-Shot Prompt: Here, a few-shot prompt template is created using the FewShotPromptTemplate class. This template includes the example prompt and allows for the generation of text for new inputs, demonstrated with "Andrea Pirlo".')
st.image('images/few_shot_example.png',caption='Few Shot Example')
st.image('images/pirlo_example.png',caption='Andrea Prilo- Few Shot Prompt')
st.write('Generating Few-Shot Examples: The code generates detailed biographies for Paulo Dybala, Robert Lewandowski, Cristiano Ronaldo, and Michael Jordan using the few-shot prompt template.')
st.image('images/few_shot_examples.png',caption='Few Shot Prompts')

st.write(html_element_7,unsafe_allow_html=True)
st.write('NLP Model Loading and Document Preparation: The spacy model en_core_web_md is loaded, and the combined text from all generated biographies is processed. Each biography is converted into a spacy doc  object, and entities are visualized using spacy displacy mechanism.')
st.image('images/spacy_load.png',caption='Load the model and create doc objects')
st.write('Functions for extracting entities and creating relationships between them are defined and utilized.')
st.write('Global Variables: Variables are initialized to store extracted entities, relationships, and related data throughout the script.')
st.write('Entity Extraction Function: This function iterates through sentences in the spacy document, extracts entities, and appends them to the all_entities list.')
st.image('images/get_entities.png',caption='Extract entities from sentence')
st.write('The create_relationships function effectively processes a DataFrame of entities extracted from sentences to identify and create relationships between these entities. By filtering out empty sentences, aggregating entities, removing duplicates, and creating pairwise relationships, the function allow to  be used for further analysis or visualization.')
st.image('images/create_relationship.png',caption='Creating relationships')
st.write('The graph_visualization function is responsible for creating and visualizing a network graph based on relationships between entities.')
st.write('The graph_visualization function creates and visualizes a network graph from a DataFrame of relationships. It includes: Constructing a NetworkX graph from a pandas DataFrame. Visualizing the graph using Matplotlib.Creating an interactive network graph with PyVis. Detecting communities within the graph using the Louvain method and visualizing the community structure in a second interactive network graph. This comprehensive approach allows for both static and interactive exploration of the relationships and community structures within the data.')
st.image('images/graph_visualization.png',caption='Graph Visualization')
st.write('This section of code prepares structured HTML and CSS elements for a Streamlit application. It defines visually appealing headers with specific styling using CSS, enhancing the presentation of project.')
st.image('images/html_objects.png',caption='Create HTML+CSS elements')
st.write('This Streamlit application facilitates interactive relation extraction and visualization for sports players. It integrates user input, natural language processing, graph creation, and data visualization to provide insights into relationships between entities extracted from player descriptions. The graphs are only visible when user typed, and submitted the chosen football player.')
st.image('images/streamlit_1.png',caption='Streamlit Interface')
st.image('images/streamlit_2.png',caption='Streamlit Interface')

st.write(html_element_8, unsafe_allow_html=True)
st.image('images/attention.png',caption='Thank You for Your attention :D')
