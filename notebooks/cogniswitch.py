from __future__ import annotations
from typing import Any, Dict, Optional

import requests

class CSAPI():
    def __init__(self,
                cs_token:str,
                OAI_token: str,
                oauth_token: str):
        if not cs_token:
            raise ValueError("Missing cs_token")
        if not OAI_token:
            raise ValueError("Missing OpenAI token")
        if not oauth_token:
            raise ValueError("Missing cogniswitch OAuth token")
    
        self.cs_token = cs_token
        self.OAI_token = OAI_token        
        self.oauth_token = oauth_token    

        self.knowledge_status_url = (
            "https://api.cogniswitch.ai:8243/cs-api/0.0.1/cs/knowledgeSource/status"
            )
        self.data_retrieval_url = (
            "https://api.cogniswitch.ai:8243/cs-api/0.0.1/cs/knowledgeRequest/data"
            )
        self.answer_url = (
            "https://api.cogniswitch.ai:8243/cs-api/0.0.1/cs/knowledgeRequest"
            )
        self.knowledgesource_file = (
            "https://api.cogniswitch.ai:8243/cs-api/0.0.1/cs/knowledgeSource/file"
            )
        self.knowledgesource_url = (
        "https://api.cogniswitch.ai:8243/cs-api/0.0.1/cs/knowledgeSource/url"
    )
    def cs_data_retrieval_api(self, query: str,
                      ) -> dict:
        """
        Send a query to the Cogniswitch service and retrieve the response.

        Args:
            query (str): Query to be answered.

        Returns:
            dict: Response JSON from the Cogniswitch service.
        """
        if not query:
            raise ValueError("Missing input query")
        
        headers = {
            "apiKey": self.oauth_token,
            "platformToken": self.cs_token,
            "openAIToken": self.OAI_token,
        }

        data = {"query": query}
        response = requests.post(self.data_retrieval_url, headers=headers, verify=False, data=data)
        return response.json()

    def answer_cs(self, query: str) -> dict:
        """
        Send a query to the Cogniswitch service and retrieve the response.

        Args:
            cs_token (str): Cogniswitch token.
            OAI_token (str): OpenAI token.
            apiKey (str): OAuth token.
            query (str): Query to be answered.

        Returns:
            dict: Response JSON from the Cogniswitch service.
        """
        if not query:
            raise ValueError("Missing input query")
        
        headers = {
            "apiKey": self.oauth_token,
            "platformToken": self.cs_token,
            "openAIToken": self.OAI_token,
        }

        data = {"query": query}
        response = requests.post(self.answer_url, headers=headers, verify=False, data=data)
        return response.json()    

    def knowledge_status(self, document_name: str) -> dict:
        """
        Use this function to know the status of the document or the URL uploaded
        Args:
            document_name (str): The document name or the url that is uploaded.

        Returns:
            dict: Response JSON from the Cogniswitch service.
        """

        params = {"docName": document_name, "platformToken": self.cs_token}
        headers = {
            "apiKey": self.oauth_token,
            "openAIToken": self.OAI_token,
            "platformToken": self.cs_token,
        }
        response = requests.get(
            self.knowledge_status_url,
            headers=headers,
            params=params,
            verify=False,
        )
        if response.status_code == 200:
            source_info = response.json()
            source_data = dict(source_info[-1])
            status = source_data.get("status")
            if status == 0:
                source_data["status"] = "SUCCESS"
            elif status == 1:
                source_data["status"] = "PROCESSING"
            elif status == 2:
                source_data["status"] = "UPLOADED"
            elif status == 3:
                source_data["status"] = "FAILURE"
            elif status == 4:
                source_data["status"] = "UPLOAD_FAILURE"
            elif status == 5:
                source_data["status"] = "REJECTED"

            if "filePath" in source_data.keys():
                source_data.pop("filePath")
            if "savedFileName" in source_data.keys():
                source_data.pop("savedFileName")
            if "integrationConfigId" in source_data.keys():
                source_data.pop("integrationConfigId")
            if "metaData" in source_data.keys():
                source_data.pop("metaData")
            if "docEntryId" in source_data.keys():
                source_data.pop("docEntryId")
            return source_data
        else:
            # error_message = response.json()["message"]
            print(response.status_code)
            return {
                "message": response.status_code,
            }

    def store_data_file(
        self,
        file: Optional[str],
        document_name: Optional[str],
        document_description: Optional[str],
    ) -> dict:
        """
        Store data using the Cogniswitch service.
        This calls the CogniSwitch services to analyze & store data from a file.
        If the input looks like a file path, assign that string value to file key.
        Assign document name & description only if provided in input.

        Args:
            file (Optional[str]): file path of your file.
            the current files supported by the files are
            .txt, .pdf, .docx, .doc, .html
            document_name (Optional[str]): Name of the document you are uploading.
            document_description (Optional[str]): Description of the document.

        Returns:
            dict: Response JSON from the Cogniswitch service.
        """
        headers = {
            "apiKey": self.oauth_token,
            "openAIToken": self.OAI_token,
            "platformToken": self.cs_token,
        }
        data: Dict[str, Any]
        if not document_name:
            document_name = ""
        if not document_description:
            document_description = ""

        files = {"file": open(file, "rb")}

        data = {
            "documentName": document_name,
            "documentDescription": document_description,
        }
        response = requests.post(
            self.knowledgesource_file,
            headers=headers,
            verify=False,
            data=data,
            files=files,
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return {"message": "Bad Request"}

    
    def store_data_url(
        self,
        url: Optional[str],
        document_name: Optional[str],
        document_description: Optional[str],
    ) -> dict:
        """
        Store data using the Cogniswitch service.
        This calls the CogniSwitch services to analyze & store data from a url.
        the URL is provided in input, assign that value to the url key.
        Assign document name & description only if provided in input.

        Args:
            url (Optional[str]): URL link.
            document_name (Optional[str]): Name of the document you are uploading.
            document_description (Optional[str]): Description of the document.

        Returns:
            dict: Response JSON from the Cogniswitch service.
        """
        headers = {
            "apiKey": self.oauth_token,
            "openAIToken": self.OAI_token,
            "platformToken": self.cs_token,
        }
        data: Dict[str, Any]
        if not document_name:
            document_name = ""
        if not document_description:
            document_description = ""
        if not url:
            return {
                "message": "No input provided",
            }
        else:
            data = {"url":url}
#             input_url = self.knowledgesource_url+f"?url={url}"
            response = requests.post(
                self.knowledgesource_url,
#                 input_url,
                headers=headers,
                verify=False,
                data=data,
            )
        if response.status_code == 200:
            return response.json()
        else:
            return response
#             print(response.status_code)
#             return {"message": "Bad Request", "error": response.status_code}


