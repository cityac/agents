#!/usr/bin/env python
# src/financial_researcher/main.py
import sys
import os
from datetime import datetime
from my_financial_researcher.crew import MyResearchCrew

# Create reports directory if it doesn't exist
os.makedirs('reports', exist_ok=True)

def run():

    company = input("Enter company name: ")

    """
    Run the research crew.
    """

    inputs = {                                                  
        'company': company,                                     
        'current_date':                                         
            datetime.now().strftime('%Y-%m-%dT%H:%M:%S')                              
    }  

    # Create and run the crew
    result = MyResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()