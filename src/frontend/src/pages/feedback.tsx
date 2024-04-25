import User from "@/components/user";
import React, { useEffect } from "react";
import CardUI from "@/components/card";
import ExpandableContent from "@/components/expandableContent";
import Tag from "@/components/tag";
import { EmailType } from "@/data/types";
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

interface FeedbackPageProps {
  feedbackData: EmailType[];
}
const getFeedbackData = async () => {
  try {
    const dataRequest = await customFetch.get("/feedbacks");
    console.log(dataRequest);
  } catch (error) {
    console.log(`Error: ${error}`);
  }
};

const FeedbackPage: React.FC<FeedbackPageProps> = ({ feedbackData }) => {
  useEffect(() => {
    getFeedbackData();
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
      {feedbackData.map((feedback) => {
        const headerComponent = (
          <div className="flex justify-between items-center">
            <span className="font-semibold">Feedback #{feedback.id}</span>
            <span className="text-gray-500">{feedback.date}</span>
          </div>
        );

        const footerComponent = (
          <div className="flex items-center justify-between flex-row bg-white text-slate-700 w-full">
            <User
              fallBack={feedback.user.name}
              imgHref={feedback.user.imgHref}
              className="mr-auto"
            />
            <Tag tagContent={feedback.category} className="mx-2" />
            <DropDown feedback={feedback} />
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
            <ExpandableContent content={feedback.content} shownNumber={40} />
          </CardUI>
        );
      })}
    </div>
  );
};

export default FeedbackPage;
