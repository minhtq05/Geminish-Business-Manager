import User from "@/components/user";
import React, { useEffect, useState } from "react";
import { FeedbackDataType } from "@/data/types";
import CardUI from "@/components/card";
import ExpandableContent from "@/components/expandableContent";
import DropDown from "@/components/dropDown";
import { Separator } from "@/components/ui/separator";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import customFetch from "@/utils/customFetch";

const FeedbackPage: React.FC = () => {
  const [dataLoaded, setDataLoaded] = useState<boolean>(false);
  const [feedbackData, setFeedbackData] = useState<FeedbackDataType[]>([
    {
      id: "",
      sender: { name: "", email: "" },
      content: { subject: "", body: "" },
      date: "",
    },
  ]);
  const getFeedbackData = async () => {
    try {
      console.log(dataLoaded);
      if (!dataLoaded) {
        const feedbackDataRequest = await customFetch.get("/feedbacks");
        const rawFeedbackData = feedbackDataRequest.request.response; // return raw backend data as a {messages : []} string

        let cleanedData: { messages: FeedbackDataType[] } = { messages: [] }; // declare an empty {messages : []} object

        // populate the messages attribute in the cleanData object
        JSON.parse(rawFeedbackData).messages.forEach((feedback: any) => {
          cleanedData.messages.push({
            id: feedback.id,
            sender: {
              name: feedback.sender.name,
              email: feedback.sender.email,
            },
            content: {
              subject: feedback.subject,
              body: feedback.body,
            },
            date: feedback.date,
          });
        });

        localStorage.setItem("feedbackData", JSON.stringify(cleanedData)); // cache as a string

        const feedbackDataString = localStorage.getItem("feedbackData");
        if (feedbackDataString) {
          setFeedbackData(JSON.parse(feedbackDataString).messages); // Parse string to object
          console.log(feedbackData);
        }
        setDataLoaded(true);
      } else {
        const cachedFeedbackDataString = await localStorage.getItem(
          "feedbackData"
        );
        if (cachedFeedbackDataString) {
          setFeedbackData(JSON.parse(cachedFeedbackDataString).messages); // Parse string to object
          console.log(feedbackData);
        }
      }
    } catch (error) {
      console.log(`Error: ${error}`);
      setDataLoaded(false);
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
      <div className="flex flex-row items-end justify-between md:w-[90%]  w-full mx-4">
        <div className="flex-grow">
          <Label htmlFor="search" className="text-4xl">
            Search
          </Label>
          <Input id="search" type="search" placeholder="Search feedback" />
        </div>
        <Select>
          <SelectTrigger className="max-w-[fit-content] ml-4">
            <SelectValue placeholder="Filter by" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectLabel>Filters</SelectLabel>
              <SelectItem value="relevance">Relevance</SelectItem>
              <SelectItem value="date">Date sent</SelectItem>
              <SelectItem value="email">Email</SelectItem>
              <SelectItem value="category">Category</SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
      {Array.isArray(feedbackData) &&
        feedbackData.map((feedback) => {
          const headerComponent = (
            <div className="flex justify-between items-center">
              <span className="font-semibold">Feedback #{feedback.id}</span>
              <span className="text-gray-500">{feedback.date}</span>
            </div>
          );

          const footerComponent = (
            <div className="flex items-center justify-between flex-row bg-white text-slate-700 w-full">
              <User fallBack={feedback.sender.name} className="mr-auto" />
              <DropDown feedback={{ user: { name: feedback.sender.name } }} />
            </div>
          );

          return (
            <CardUI
              className="md:w-[90%] w-full overflow-x-visible drop-shadow-sm flexcard"
              colorScheme={{
                bgColor: "bg-white",
                textColor: "text-slate-600",
              }}
              key={feedback.id}
              headerComponent={headerComponent}
              footerComponent={footerComponent}
            >
              <ExpandableContent
                content={{
                  heading: feedback.content.subject,
                  body: feedback.content.body,
                }}
                shownNumber={40}
              />
            </CardUI>
          );
        })}
    </div>
  );
};

export default FeedbackPage;
