import User from "@/components/user";
import React from "react";
import CardUI from "@/components/card";
import ExpandableContent from "@/components/expandableContent";
import Tag from "@/components/tag";
import { EmailType } from "@/data/types";
import { Button } from "@/components/ui/button"
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
} from "@/components/ui/dropdown-menu"
 

interface FeedbackPageProps {
  feedbackData: EmailType[];
}

const FeedbackPage: React.FC<FeedbackPageProps> = ({ feedbackData }) => {
  return (
    <div
      className="flex flex-col justify-evenly items-center gap-4 h-[100dvh] overflow-auto py-4"
      id="email-container"
    >
      {feedbackData.map((feedback) => {
        const headerComponent = (
          <div className="flex justify-between items-center">
            <span className="font-semibold">Feedback #{feedback.id}</span>
            <span className="text-gray-500">{feedback.date}</span>
          </div>
        );

        const footerComponent = (
          <div className="flex items-center justify-between flex-row bg-slate-50 text-slate-700 w-full">
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
                  <span>Profile</span>
                <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
              </DropdownMenuItem>
            </DropdownMenuGroup>
            </DropdownMenuContent>
            </DropdownMenu>
          </div>
        );

        return (
          <CardUI
            className="md:w-[90%] w-[100%] max-w-[max-content]"
            colorScheme={{
              bgColor: "bg-slate-50",
              textColor: "text-slate-700",
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
  );
};

export default FeedbackPage;
