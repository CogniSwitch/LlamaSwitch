# LlamaSwitch
## [Use CogniSwitch with LlamaIndex](https://github.com/CogniSwitch/LlamaSwitch/tree/main#use-cogniswitch-with-llamaindex)
No GenAI experience required! Skip the classroom and courses and get started on building your own GenAI applications using CogniSwitch. Using its unique automated pipeline, CogniSwitch helps developers build GenAI applications by: 

💨 Speeding up GenAI development  

⚙️ Handling decisions related to ICP (Ingestion, Curation & Procurement) of knowledge/Information 

🪄Drastically reduces hallucinations of LLMs  

🎯 Improves accuracy of responses generated 

🚀 Only takes 3 simple steps to get started 

To help LLamaIndex users conquer generative AI, we’ve put together “LlamaSwitch” that helps seamlessly integrate with CogniSwitch to develop state of the art GenAI applications. 

Become A GenAI Developer now: [Signup (cogniswitch.ai)](https://console.cogniswitch.ai:8443)  

Learn more about CogniSwitch: [https://www.cogniswitch.ai/developer](https://www.cogniswitch.ai/developer?utm_source=llamaindex&utm_medium=llamaindexbuild&utm_id=dev) 

**Step 1: Instantiate the Cogniswitch ToolSpec:**
- Use your Cogniswitch token, openAI API key, OAuth token to instantiate the toolspec.  

**Step 2: Cogniswitch Store data:**
- Use store_data function in the toolspec and input your file or url. 
- Currently we support PDF(.pdf), Word(.docx, .doc), text(.txt), HTML(.html) file formats. (more formats are coming)
- It will be processed and stored in your knowledge store. 
- You can check the status of document processing in cogniswitch console. 

**Step 3: Cogniswitch Answer:**
- Use query_knowledge function in the toolspec and input your query. 
- You will get the answer from your knowledge as the response. 

## [Customize your own cogniswitch tool](https://github.com/CogniSwitch/LlamaSwitch/tree/main#customize-your-own-cogniswitch-tool)

- In order to use the cogniswitch toolspec you need to get the "llamaswitch" folder from the repository and put it in the same directory as notebook and import the tool as shown in the [notebook](https://github.com/CogniSwitch/LlamaSwitch/blob/main/notebooks/CogniswitchToolSpec_source.ipynb).

**Use the example notebook to try the cogniswitch tool from [here](https://github.com/CogniSwitch/LlamaSwitch/blob/main/notebooks/CogniswitchToolSpec_source.ipynb)**

## [Customize your own cogniswitch query engine](https://github.com/CogniSwitch/LlamaSwitch/tree/main#customize-your-own-cogniswitch-query-engine)

- In order to use the cogniswitch query engine you need to get the "llamaswitch" folder from the repository and put it in the same directory as notebook and import the query engine as shown in the [notebook](https://github.com/CogniSwitch/LlamaSwitch/blob/main/notebooks/CogniswitchQueryEngine_source.ipynb).

**Use the example notebook to try the cogniswitch query engine from [here](https://github.com/CogniSwitch/LlamaSwitch/blob/main/notebooks/CogniswitchQueryEngine_source.ipynb)**