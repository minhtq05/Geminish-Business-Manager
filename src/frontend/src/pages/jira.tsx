
import React, { useEffect, useState } from "react";
import CardUI from "@/components/card";
import ExpandableContent from "@/components/expandableContent";
import { Separator } from "@/components/ui/separator";
import customFetch from "@/utils/customFetch";

interface JiraDataType {
  fields: {
    summary: string;
    description: string;
  };
}

const JiraPage: React.FC = () => {
  const [jiraData, setJiraData] = useState<JiraDataType[]>([]);

  const getJiraData = async () => {
    try {
      const search = new URLSearchParams();
      search.append("project_key", "ARP");
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
    // localStorage.clear();
  }, []);
  return (
    <div
      className="bg-[#F9F9F9] flex flex-col justify-start items-center gap-8 h-[100dvh] py-4 overflow-y-auto"
      id="email-container"
    >
      <h1 className="text-4xl font-bold text-indigo-600">Jira</h1>
      <Separator />
      {jiraData.map((data: JiraDataType, index: number) => {
        return (
          <CardUI
            className="w-3/4"
            key={index}
            headerComponent={data.fields.summary}
            colorScheme={{ bgColor: "bg-white", textColor: "text-black" }}
          >
            {/* <ExpandableContent content={data.fields.description} /> */}
            <p>{data.fields.description}</p>
          </CardUI>
        );
      })}
    </div>
  );
};

export default JiraPage;
