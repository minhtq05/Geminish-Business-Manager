import { EmailType } from "@/data/types";
import { FaUser } from "react-icons/fa";
import { MdOutlineFeedback } from "react-icons/md";
import { FaRegTrashAlt } from "react-icons/fa";
import { HiOutlineDotsHorizontal } from "react-icons/hi";
import { cn } from "@/lib/utils";

interface TagProps {
  tagContent: EmailType["category"];
  className?: string;
}
const Tag: React.FC<TagProps> = ({ tagContent, className }: TagProps) => {
  // client blue
  // feedback green
  // spam gray
  // others golden
  const tagBGColor = {
    client: "bg-blue-100",
    feedback: "bg-green-100",
    spam: "bg-gray-100",
    others: "bg-yellow-100",
  };
  const tagTextColor = {
    client: "text-blue-500",
    feedback: "text-green-500",
    spam: "text-gray-500",
    others: "text-yellow-500",
  };
  const tagIcon = {
    client: <FaUser />,
    feedback: <MdOutlineFeedback />,
    spam: <FaRegTrashAlt />,
    others: <HiOutlineDotsHorizontal />,
  };
  return (
    <div
      className={cn(
        "subpixel-antialiased font-semibold tracking-wide flex flex-row items-center px-4 py-2 rounded-md gap-2",
        tagBGColor[tagContent],
        className
      )}
    >
      {tagIcon[tagContent]}
      <span className={cn("tag", tagTextColor[tagContent])}>{tagContent}</span>
    </div>
  );
};
export default Tag;
