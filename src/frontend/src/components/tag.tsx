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
const Tag: React.FC<TagProps> = ({ tagContent, className } : TagProps) => {
    // client blue
    // feedback green
    // spam gray
    // others golden
    const tagBGColor = {
        client: "bg-blue-200",
        feedback: "bg-green-200",
        spam: "bg-gray-200",
        others: "bg-yellow-200",
    };
    const tagTextColor = {
        client: "text-blue-600",
        feedback: "text-green-600",
        spam: "text-gray-600",
        others: "text-yellow-600",
    };
    const tagIcon = {
        client: <FaUser />,
        feedback: <MdOutlineFeedback />,
        spam: <FaRegTrashAlt />,
        others: <HiOutlineDotsHorizontal />,
    }
    return(
        <div className={cn("subpixel-antialiased font-semibold tracking-wide flex flex-row items-center px-4 py-2 rounded-md gap-2", tagBGColor[tagContent], className)}>
            {tagIcon[tagContent]}
            <span className={cn("tag", tagTextColor[tagContent])}>{tagContent}</span>
        </div>
    )
}
export default Tag;