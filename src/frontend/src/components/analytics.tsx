import CardUI from "./card";
import { cn } from "@/lib/utils";
import { AnalyticText } from "@/data/types";
interface AnalyticsProps {
  className?: string;
  content: AnalyticText[];
}
const Analytics: React.FC<AnalyticsProps> = ({ className, content }) => {
  return (
    <div
      className={cn(
        "flex-1 flex flex-col items-center justify-evenly",
        className
      )}
    >
      {content.map((text) => {
        return (
          <CardUI headerComponent={text.heading}>
            <p>{text.content}</p>
          </CardUI>
        );
      })}
    </div>
  );
};
export default Analytics;
