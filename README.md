# LlamaSwitch
## Use CogniSwitch with LlamaIndex
**Use CogniSwitch to build production ready applications that can consume, organize and retrieve knowledge flawlessly. Using the framework of your choice, in this case LlamaIndex, CogniSwitch helps alleviate the stress of decision making when it comes to, choosing the right storage and retrieval formats. It also eradicates reliability issues and hallucinations when it comes to responses that are generated. Get started by interacting with your knowledge in just three simple steps**

Visit [https://www.cogniswitch.ai/developer](https://www.cogniswitch.ai/developer?utm_source=llamaindex&utm_medium=llamaindexbuild&utm_id=dev)

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

## Customize your own cogniswitch tool

- In order to use the cogniswitch toolspec you need to get the "llamaswitch" folder from the repository and put it in the same directory as notebook and import the tool as shown in the notebook.

**Use the example notebook to try the cogniswitch tool from [here](https://github.com/CogniSwitch/LlamaSwitch/blob/main/notebooks/CogniswitchToolSpec_source.ipynb)**

## Customize your own cogniswitch query engine

- In order to use the cogniswitch query engine you need to get the "llamaswitch" folder from the repository and put it in the same directory as notebook and import the query engine as shown in the notebook.

**Use the example notebook to try the cogniswitch query engine from [here](https://github.com/CogniSwitch/LlamaSwitch/blob/main/notebooks/CogniswitchQueryEngine_source.ipynb)**