
import React, { useState } from "react";
import { cn } from "@/lib/utils";
interface ExpandableComponentProps {
  content: { heading?: string; body: string };
  className?: string;
  shownNumber?: number;
  showsFull?:boolean;
}
const ExpandableComponent: React.FC<ExpandableComponentProps> = ({
  content,
  className,
  shownNumber,
  showsFull,
}: ExpandableComponentProps) => {
  shownNumber = shownNumber ? shownNumber : 30;
  const canHide = shownNumber < content.body.split(" ").length;
  const truncatedText = canHide
    ? content.body.split(" ").slice(0, shownNumber).join(" ")
    : content.body;
  const [blurredText, setBlurredText] = useState<boolean>(true);
  return (
    <div className={cn("w-full", className)}>
      <h1 className="text-2xl text-gray-700 font-bold my-2">{content.heading}</h1>
      <span className={cn("text-slate-500 text-xl", blurredText && !showsFull ? "text-slate-500" : "text-slate-900" )}>
        {blurredText && !showsFull ? truncatedText + "... " : content.body}
        {showsFull ? null : <span className="text-blue-400" onClick={()=>{setBlurredText(!blurredText)}}>{blurredText ? " Show more" : " Show less"}</span>}
      </span>
    </div>
  );
};
export default ExpandableComponent;
