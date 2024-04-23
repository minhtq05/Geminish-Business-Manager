import User from "@/components/user";
import React from "react";
import CardUI from "@/components/card";
import ExpandableContent from "@/components/expandableContent";
import Tag from "@/components/tag";
import { EmailType } from "@/data/types";
import { Button } from "@/components/ui/button";
import { CiMail } from "react-icons/ci";
import { BiTask } from "react-icons/bi";
import { FaRegTrashAlt } from "react-icons/fa";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuPortal,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
interface FeedbackPageProps {
  feedbackData: EmailType[];
}

const FeedbackPage: React.FC<FeedbackPageProps> = ({ feedbackData }) => {
  return (
    <div
      className=" bg-[#F9F9F9] flex flex-col justify-start w-full items-start gap-8 h-[100dvh] py-4 px-2 overflow-y-auto"
      id="email-container"
    >
      <div className="flex items-center justify-between flex-row gap-4 w-full">
        <Input type="text" placeholder="Search with email or keywords" />
        <Select>
          <SelectTrigger>
            <SelectValue placeholder="Sort by" />
          </SelectTrigger>
          <SelectContent>
            <SelectGroup>
              <SelectLabel>Filters</SelectLabel>
              <SelectItem value="name">Name</SelectItem>
              <SelectItem value="date">Date sent</SelectItem>
              <SelectItem value="relevance">Relevance</SelectItem>
              <SelectItem value="tag">Tag</SelectItem>
            </SelectGroup>
          </SelectContent>
        </Select>
      </div>
      <div className="w-full flex flex-col items-start justify-start gap-8">
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
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="outline">Open</Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent className="w-56">
                  <DropdownMenuLabel>{feedback.category}</DropdownMenuLabel>
                  <DropdownMenuSeparator />
                  <DropdownMenuGroup>
                    <DropdownMenuItem>
                      <User
                        fallBack={feedback.user.name}
                        imgHref={feedback.user.imgHref}
                      />
                      <span className="mx-2">Profile</span>
                      <DropdownMenuShortcut>⇧⌘ P</DropdownMenuShortcut>
                    </DropdownMenuItem>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem>
                      <CiMail />
                      <span className="mx-2">Email</span>
                      <DropdownMenuShortcut>⇧⌘ M</DropdownMenuShortcut>
                    </DropdownMenuItem>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem>
                      <BiTask />
                      <span className="mx-2">Set up Jira Task</span>
                      <DropdownMenuShortcut>⇧⌘ J</DropdownMenuShortcut>
                    </DropdownMenuItem>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem>
                      <FaRegTrashAlt />
                      <span className="mx-2">Delete</span>
                      <DropdownMenuShortcut>⇧⌘ D</DropdownMenuShortcut>
                    </DropdownMenuItem>
                  </DropdownMenuGroup>
                </DropdownMenuContent>
              </DropdownMenu>
            </div>
          );

          return (
            <CardUI
              className="md:w-[85%] overflow-x-visible drop-shadow-sm flexcard"
              colorScheme={{
                bgColor: "bg-white",
                textColor: "text-slate-600",
              }}
              key={feedback.id}
              headerComponent={headerComponent}
              footerComponent={footerComponent}
            >
              <ExpandableContent content={feedback.content} />
            </CardUI>
          );
        })}
      </div>
    </div>
  );
};

export default FeedbackPage;
