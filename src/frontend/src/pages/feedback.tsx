import User from "@/components/user";
import React from "react";
import CardUI from "@/components/card";
import ExpandableContent from "@/components/expandableContent";
import { feedbackType } from "@/data/types";

interface FeedbackPageProps {
  feedbackData: feedbackType[];
}

const FeedbackPage: React.FC<FeedbackPageProps> = ({ feedbackData }) => {
  return (
    <div
      className="flex flex-col justify-evenly items-center gap-4 overscroll-auto overflow-y-auto "
      id="email-container"
    >
      {feedbackData.map((feedback) => {
        const headerComponent = (
          <div className="flex justify-between items-center">
            <span>{feedback.id}</span>
            <span className="text-gray-500">{feedback.time}</span>
          </div>
        );

        const footerComponent = (
          <div className="flex justify-between items-center bg-slate-50 text-slate-700">
            <User
              fallBack={feedback.user.name}
              imgHref={feedback.user.imgHref}
            />
            <div>
              {feedback.tags.map((tag) => (
                <span>{tag}</span>
              ))}
            </div>
          </div>
        );

        return (
          <CardUI
            className="max-w-[90%]"
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
