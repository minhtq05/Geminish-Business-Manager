import React, { useEffect, useState } from "react";
import CardUI from "@/components/card";
import { Separator } from "@/components/ui/separator";
import customFetch from "@/utils/customFetch";
import { Button } from "@/components/ui/button";
import BlackCheck from "@/assets/black_check.png";
import { Terminal } from "lucide-react";

import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";

interface JiraDataType {
  fields: {
    summary: string;
    description: string;
  };
}

const JiraPage: React.FC = () => {
  const [jiraData, setJiraData] = useState<JiraDataType[]>([]);
  const [selectedCards, setSelectedCards] = useState<Set<number>>(new Set());
  const [showAlert, setShowAlert] = useState(false);
  const [alertMessage, setAlertMessage] = useState("");

  const handleCardSelection = (index: number) => {
    if (selectedCards.has(index)) {
      setSelectedCards((prevState) => {
        const newSet = new Set(prevState);
        newSet.delete(index);
        return newSet;
      });
    } else {
      setSelectedCards((prevState) => new Set(prevState.add(index)));
    }
  };

  const handleSubmit = async () => {
    try {
      const selectedJiraData = Array.from(selectedCards).map((index) => {
        const { fields } = jiraData[index];
        return { fields };
      });

      // Not allow to submit empty data
      if (selectedJiraData.length === 0) {
        setShowAlert(true);
        setAlertMessage("Please select a Jira ticket to submit");
        return;
      }

      const sendRequestBody = { tickets: selectedJiraData };

      const response = await customFetch.post("/jira/upload", sendRequestBody);
      console.log(response);
      setShowAlert(true);
      setAlertMessage("Jira ticket submitted successfully!");
      // empty the selected cards
      setSelectedCards(new Set());
    } catch (error) {
      console.log(error);
      setShowAlert(true);
      setAlertMessage("Failed to submit Jira ticket");
    }
  };

  const getJiraData = async () => {
    try {
      const search = new URLSearchParams();
      search.append("project_key", "ARP");
      const mockData = {
        tickets: [
          {
            fields: {
              project: {
                key: "ARP",
              },
              summary:
                "Black Coffee: Improve the richness and boldness of the coffee",
              description:
                "Explore using different coffee bean origins or roasting techniques to enhance the depth and complexity of the flavor.",
              issuetype: {
                name: "Task",
              },
            },
          },
          {
            fields: {
              project: {
                key: "ARP",
              },
              summary: "Black Coffee: Reduce bitterness",
              description:
                "Experiment with different brewing methods or adjust the coffee-to-water ratio to achieve a smoother, less bitter taste.",
              issuetype: {
                name: "Task",
              },
            },
          },
          {
            fields: {
              project: {
                key: "ARP",
              },
              summary: "Black Coffee: Offer different roast options",
              description:
                "Provide customers with a choice of light, medium, or dark roasts to cater to varying preferences for coffee strength and flavor profiles.",
              issuetype: {
                name: "Task",
              },
            },
          },
          {
            fields: {
              project: {
                key: "ARP",
              },
              summary: "White Coffee: Reduce sweetness",
              description:
                "Adjust the amount of sugar or sweetener used to create a more balanced flavor that allows the coffee notes to shine through.",
              issuetype: {
                name: "Task",
              },
            },
          },
          {
            fields: {
              project: {
                key: "ARP",
              },
              summary:
                "White Coffee: Offer sugar-free or alternative sweetener options",
              description:
                "Cater to customers who prefer to control their sugar intake or have dietary restrictions by providing sugar-free syrups or alternative sweeteners.",
              issuetype: {
                name: "Task",
              },
            },
          },
          {
            fields: {
              project: {
                key: "ARP",
              },
              summary:
                "White Coffee: Experiment with different types of milk or cream",
              description:
                "Explore using different milk options, such as oat milk, almond milk, or lactose-free milk, to cater to customers with dietary preferences or restrictions. Additionally, consider offering different cream options with varying fat contents to allow customers to customize the richness and texture of their white coffee.",
              issuetype: {
                name: "Task",
              },
            },
          },
        ],
      };
      setJiraData(mockData["tickets"]);
      return;
      const JiraDataRequest = await customFetch.get("/jira", {
        params: search,
      });
      console.log(JSON.parse(JiraDataRequest.request.response));
      if (JiraDataRequest.status !== 200) {
        throw new Error("Failed to fetch data");
      }
      if (!("tickets" in JSON.parse(JiraDataRequest.request.response))) {
        throw new Error("Invalid response");
      }

      setJiraData(JSON.parse(JiraDataRequest.request.response)["tickets"]);
      console.log(jiraData);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    if (process.env.NODE_ENV === "development") {
      getJiraData();
    }
  }, []);

  useEffect(() => {
    console.log(selectedCards);
  }, [selectedCards]);
  return (
    <div
      className="bg-[#F9F9F9] flex flex-col justify-start items-center gap-8 h-[100dvh] py-4 overflow-y-auto"
      id="email-container"
    >
      <h1 className="text-4xl font-bold text-indigo-600">Jira</h1>
      <Separator />
      {showAlert && (
        <Alert className="bg-[#F9F9F9]">
          <Terminal className="h-4 w-4" />
          <AlertTitle>Submission Status</AlertTitle>
          <AlertDescription>{alertMessage}</AlertDescription>
        </Alert>
      )}
      {jiraData.map((data: JiraDataType, index: number) => {
        const isSelected = selectedCards.has(index);
        return (
          <div className="w-3/4 relative" key={index}>
            <CardUI
              className="w-full"
              headerComponent={data.fields.summary}
              colorScheme={{ bgColor: "bg-white", textColor: "text-black" }}
            >
              <p>{data.fields.description}</p>
            </CardUI>
            {isSelected && (
              <img
                src={BlackCheck}
                alt="selected"
                className="absolute right-[1.25rem] top-1/2 transform -translate-y-1/2 w-[2.5rem] h-[2.5rem]"
              />
            )}
            <div
              className="absolute inset-0 bg-transparent"
              onClick={() => handleCardSelection(index)}
            />
          </div>
        );
      })}
      <Button className="absolute bottom-8 right-16" onClick={handleSubmit}>
        Submit
      </Button>
    </div>
  );
};

export default JiraPage;
