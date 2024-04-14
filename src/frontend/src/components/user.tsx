import {
    Avatar,
    AvatarFallback,
    AvatarImage,
} from "@/components/ui/avatar"

interface UserProps{
    imgHref:string,
    altText?:string,
    fallBack:string,
}
const User: React.FC<UserProps> = ({imgHref, fallBack, altText} : UserProps) => {
    return(
        <Avatar>
            <AvatarImage src={imgHref} alt={altText ? altText : "User img"} />
            <AvatarFallback>{fallBack}</AvatarFallback>
        </Avatar>
    )
}
export default User