import ShowMoreText from "react-show-more-text";
import React, { useState } from "react";
import { cn } from "@/lib/utils";
interface ExpandableComponentProps {
  content: { heading?: string; body: string };
  className?: string;
  shownNumber?: number;
}
const ExpandableComponent: React.FC<ExpandableComponentProps> = ({
  content,
  className,
  shownNumber,
}: ExpandableComponentProps) => {
  shownNumber = shownNumber ? shownNumber : 20;
  const canHide = shownNumber < content.body.split(" ").length;
  const truncatedText = canHide
    ? content.body.split(" ").slice(0, shownNumber).join(" ")
    : content.body;
  return (
    <div className={cn("expand-content overflow-visible w-[90%]", className)}>
      <h1 className="text-2xl text-gray-700 font-bold">{content.heading}</h1>
      <p className="text-slate-500 text-xl">
        {canHide ? truncatedText + "... " : content.body}
        <span className="text-blue-400">{canHide ? "Learn more" : ""}</span>
      </p>
      {/* <ShowMoreText
        lines={3}
        more="Show more"
        less="Show less"
        anchorClass="text-blue-500"
        truncatedEndingComponent={"... "}
        expanded={false}
        className={cn(
          "vertical-expandable-text",
          blurredText ? "text-slate-500" : "text-slate-900"
        )}
        onClick={() => setBlurredText(!blurredText)}
      > */}
      {/* {content.body}
      </ShowMoreText> */}
    </div>
  );
};
export default ExpandableComponent;
