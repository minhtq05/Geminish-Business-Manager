import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuTrigger,
  } from "@/components/ui/dropdown-menu";
import {Button} from "@/components/ui/button"
import { CiMail } from "react-icons/ci";
import { BiTask } from "react-icons/bi";
import { FaRegTrashAlt } from "react-icons/fa";
import User from "./user";

interface DropDownProps {
    feedback:{
        category:string,
        user:{
            name:string,
            imgHref:string,
        }
    }
}

const DropDown:React.FC<DropDownProps> = ({feedback} : DropDownProps) => {
    return(
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
    )
}
export default DropDown;