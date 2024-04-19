import User from "@/components/user";
import React from "react";
import CardUI from "@/components/card";
import ExpandableContent from "@/components/expandableContent";
import { feedbackType } from "@/data/types";


interface FeedbackPageProps{
  feedbackData: feedbackType[];
}
const FeedbackPage: React.FC<FeedbackPageProps> = ({feedbackData}) => {
  return(
    <main className="flex flex-col justify-evenly items-center gap-4">
      {feedbackData.map(feedback => {
        return(
          <CardUI colorScheme={{bgColor:"bg-slate-50", textColor:"text-slate-700"}} key={feedback.id} headerComponent={<div className="flex justify-between items-center"><span>{feedback.id}</span>, <span className="text-gray-500">{feedback.time}</span></div>} footerComponent={<div className="flex justify-between items-center bg-slate-50 text-slate-700">{feedback.user} <div>{feedback.tags.map(tag=><span>{tag}</span>)}</div></div>}>
            <ExpandableContent content={feedback.content} />
          </CardUI>
        )
      })}
    </main>
  )
}
export default FeedbackPage;