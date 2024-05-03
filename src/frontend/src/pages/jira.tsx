import User from "@/components/user";
import React, { useEffect, useState } from "react";
import { FeedbackDataType } from "@/data/types";
import CardUI from "@/components/card";
import ExpandableContent from "@/components/expandableContent";
import DropDown from "@/components/dropDown";
import { Separator } from "@/components/ui/separator";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import customFetch from "@/utils/customFetch";

const JiraPage: React.FC = () => {
  const [jiraData, setJiraData] = useState<{}[]>([]);

  const getFeedbackData = async () => {
    try {
      const search = new URLSearchParams();
      search.append("project_key", "ARP");
      const JiraDataRequest = await customFetch.get("/jira", {
        params: search,
      });
      setJiraData(JSON.parse(JiraDataRequest.request.response)["tickets"]);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getFeedbackData();
    // localStorage.clear();
  }, []);
  return (
    <div
      className="bg-[#F9F9F9] flex flex-col justify-start items-center gap-8 h-[100dvh] py-4 overflow-y-auto"
      id="email-container"
    >
      <h1 className="text-4xl font-bold text-indigo-600">Feedbacks</h1>
      <Separator />
      {jiraData.map((data: any, index: number) => {
        return (
          <CardUI
            key={index}
            headerComponent={data.fields.summary}
            colorScheme={{ bgColor: "bg-white", textColor: "text-black" }}
          >
            <ExpandableContent content={data.fields.description} />
          </CardUI>
        );
      })}
    </div>
  );
};

export default JiraPage;
