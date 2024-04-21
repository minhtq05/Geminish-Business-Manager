import ShowMoreText from "react-show-more-text";
import React, {useState} from "react";
import {cn} from "@/lib/utils";
interface ExpandableComponentProps {
  content: { heading?: string; body: string };
  className?: string;
}
const ExpandableComponent: React.FC<ExpandableComponentProps> = ({
  content, className
}: ExpandableComponentProps) => {
  const [blurredText, setBlurredText] = useState<boolean>(true);
  return (
    <div className={cn("expand-content", className)}>
      <h1 className="text-2xl font-semibold">{content.heading}</h1>
      <ShowMoreText
        lines={2}
        more="Show more"
        less="Show less"
        anchorClass="text-blue-500"
        truncatedEndingComponent={"... "}
        expanded={false}
        className={cn("vertical-expandable-text", blurredText ? "text-slate-500" : "text-slate-900")}
        onClick={() => setBlurredText(!blurredText)}
        width={1500}
      >
        {content.body}
      </ShowMoreText>
    </div>
  );
};
export default ExpandableComponent;
