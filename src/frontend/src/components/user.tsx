import {
    Avatar,
    AvatarFallback,
    AvatarImage,
} from "@/components/ui/avatar"
import {cn} from "@/lib/utils"
interface UserProps{
    imgHref?:string,
    altText?:string,
    fallBack:string,
    className?:string,
}
const User: React.FC<UserProps> = ({imgHref, fallBack, altText, className} : UserProps) => {
    return(
        <Avatar className={cn("none", className)}>
            <AvatarImage src={imgHref ? imgHref : "https://github.com/shadcn.png"} alt={altText ? altText : "User img"} />
            <AvatarFallback>{fallBack}</AvatarFallback>
        </Avatar>
    )
}
export default User