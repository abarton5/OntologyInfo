#!/usr/bin/env python

"""
MIT License

Copyright (c) 2024 Adam Barton

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
def getURL(ontology, property=""):
     return f"https://www.ebi.ac.uk/ols/api/ontologies/{ontology}/{property}"


def printOntology(ontology, json):
    print("=====================")
    print(f"Ontology: {ontology}")
    print(f"The complete title for {ontology} is: ", json["config"]["title"])
    print(f"The description for {ontology} is: ", json["config"]["description"])
    print(f"The number of terms is: ", json["numberOfTerms"])
    print(f"THe current status is : ", json["status"])
    print("=====================")

def getOntInfo(ontology, debug=False):
        import requests
        api_url = getURL(ontology)
        response = requests.get(api_url)
        if response.status_code != 200:
            print(f"the request for {ontology} returned an invalid reponse - code ", response.status_code)
            return
        json = response.json()
        if debug:
            print(response.text)
            print(response.json())
        printOntology(ontology, json)

getOntInfo("agro")
getOntInfo("efo")